from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
import datetime
from django.db import connection
import pytz #para poder hacer la suma de los campos
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from .formReporteClientes import *
def not_in_AdministradorSistema_group(user):
    if user:
        return user.groups.filter(name='AdministradorSistema').count() != 0
    return False
@login_required
@user_passes_test(not_in_AdministradorSistema_group, login_url='denegado')

def Clientes(request):
    if request.method == 'POST':
        form_check=Form_Busqueda_Checbox(request.POST)
        form_fecha=Form_Busqueda_Fechas(request.POST)
        form_cliente=Form_Busqueda_Cliente(request.POST)
        fechaini = request.POST.get('fechainicial_precio')
        fechafini = request.POST.get('fechafinal_precio')
        cliente = request.POST.get('cliente_idcliente')
        truncate_date = connection.ops.date_trunc_sql('month', 'fecha_venta') #se obtiene solo el mes de la venta
        qs = Venta.objects.extra({'month':truncate_date}) # se añade un nuevo campo/columna que tendrá de nombre "month" y tendrá como datos "truncate_date" que en este caso es el mes
        fecha1=fechaini #debe ser la fecha más pequeña
        fecha2=fechafini #debe ser la fecha más grande
        fecha1_split=fecha1.split('/')
        fecha2_split=fecha2.split('/')
        compras_clientes=compras_clientes=qs.values('month','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('month') #este y funciona con las horas
        if len(fecha1_split)>1 and len(fecha2_split)>1:
            fecha1_split=fecha1.split('/')
            fecha2_split=fecha2.split('/')
            fechainicial_real=datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),0,0,0,tzinfo=pytz.UTC)
            fechafinal_real=datetime.datetime(int(fecha2_split[2]),int(fecha2_split[1]), int(fecha2_split[0]),23,59,59,tzinfo=pytz.UTC)
            fechainicial_real=fechainicial_real+datetime.timedelta(hours=6)
            fechafinal_real=fechafinal_real+datetime.timedelta(hours=6)
            box = request.POST.get('checkbo', False)
            if not cliente:
                cliente=0
            if box:
                compras_clientes = qs.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1,cliente_idcliente=int(cliente),fecha_venta__range=(fechainicial_real, fechafinal_real)).values('month','cliente_idcliente__nit_cliente','cliente_idcliente__pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('month')
                if not compras_clientes:
                    compras_clientes= qs.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1,fecha_venta__range=(fechainicial_real, fechafinal_real)).values('month','cliente_idcliente__nit_cliente','cliente_idcliente__pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('month') #este y funciona con las horas
            else:
                compras_clientes = Venta.objects.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1,cliente_idcliente=int(cliente),fecha_venta__range=(fechainicial_real, fechafinal_real)).values('cliente_idcliente__nit_cliente','cliente_idcliente__pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')
                if not compras_clientes:
                    compras_clientes = Venta.objects.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1,fecha_venta__range=(fechainicial_real, fechafinal_real)).values('cliente_idcliente__nit_cliente','cliente_idcliente__pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')

        #form_fecha=Form_Busqueda_Fechas()
        #form_cliente=Form_Busqueda_Cliente()
        #form_check=Form_Busqueda_Checbox()
        reporte1=ClientesTabla(compras_clientes)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReportesClientes.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_cliente':form_cliente,'form_check':form_check})
    else:
        form_fecha=Form_Busqueda_Fechas()
        form_cliente=Form_Busqueda_Cliente()
        form_check=Form_Busqueda_Checbox()
        consulta=Venta.objects.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1).values('cliente_idcliente__nit_cliente','cliente_idcliente__pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')
        reporte1=ClientesTabla(consulta)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReportesClientes.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_cliente':form_cliente,'form_check':form_check})
