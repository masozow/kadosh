from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum, Count
from django.utils import timezone
import datetime
from django.db import connection
import pytz #para poder hacer la suma de los campos
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from .formReporteClientes import *
@login_required

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
            box = request.POST.get('checkbo', False)
            if not cliente:
                cliente=0
            if box:
                compras_clientes = qs.filter(cliente_idcliente=cliente,fecha_venta__range=(datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),0,0,0,tzinfo=pytz.UTC), datetime.datetime(int(fecha2_split[2]),int(fecha2_split[1]), int(fecha2_split[0]),23,59,59,tzinfo=pytz.UTC))).values('month','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('month') #este y funciona con las horas
                if not compras_clientes:
                    compras_clientes= qs.filter(fecha_venta__range=(datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),0,0,0,tzinfo=pytz.UTC), datetime.datetime(int(fecha2_split[2]),int(fecha2_split[1]), int(fecha2_split[0]),23,59,59,tzinfo=pytz.UTC))).values('month','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('month') #este y funciona con las horas
            else:
                compras_clientes = Venta.objects.filter(cliente_idcliente=cliente,fecha_venta__range=(datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),0,0,0,tzinfo=pytz.UTC), datetime.datetime(int(fecha2_split[2]),int(fecha2_split[1]), int(fecha2_split[0]),23,59,59,tzinfo=pytz.UTC))).values('cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')
                if not compras_clientes:
                    compras_clientes = Venta.objects.filter(fecha_venta__range=(datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),0,0,0,tzinfo=pytz.UTC), datetime.datetime(int(fecha2_split[2]),int(fecha2_split[1]), int(fecha2_split[0]),23,59,59,tzinfo=pytz.UTC))).values('cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')

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
        consulta=Cliente.objects.all()
        reporte1=ClientesTabla(consulta)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReportesClientes.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_cliente':form_cliente,'form_check':form_check})
