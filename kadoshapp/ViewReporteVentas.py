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
from .formReporteVentas import *
from datetime import timedelta

def not_in_AdministradorSistema_group(user):
    if user:
        return user.groups.filter(name='AdministradorSistema').count() != 0
    return False

@login_required
@user_passes_test(not_in_AdministradorSistema_group, login_url='denegado')
def Ventas(request):
    if request.method == 'POST':
        form_check=Form_Busqueda_Checbox(request.POST)
        form_fecha=Form_Busqueda_Fechas(request.POST)
        form_vendedor=Form_Busqueda_Vendedor(request.POST)
        fechaini = request.POST.get('fechainicial_precio')
        fechafini = request.POST.get('fechafinal_precio')
        empleado = request.POST.get('empleado_idempleado')
        truncate_date = connection.ops.date_trunc_sql('month', 'fecha_venta') #se obtiene solo el mes de la venta
        qs = Venta.objects.extra({'month':truncate_date}) # se añade un nuevo campo/columna que tendrá de nombre "month" y tendrá como datos "truncate_date" que en este caso es el mes
        fecha1=fechaini #debe ser la fecha más pequeña
        fecha2=fechafini #debe ser la fecha más grande
        fecha1_split=fecha1.split('/')
        fecha2_split=fecha2.split('/')
        ventas_vendedor=qs.values('month','vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('month','total_ventas')
        if len(fecha1_split)>1 and len(fecha2_split)>1:
            fechainicial_real=datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),0,0,0,tzinfo=pytz.UTC)
            fechafinal_real=datetime.datetime(int(fecha2_split[2]),int(fecha2_split[1]), int(fecha2_split[0]),23,59,59,tzinfo=pytz.UTC)
            fechainicial_real=fechainicial_real+datetime.timedelta(hours=6)
            fechafinal_real=fechafinal_real+datetime.timedelta(hours=6)
            box = request.POST.get('checkbo', False)
            if not empleado:
                empleado=0
            if box:
                ventas_vendedor = qs.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1,vendedor_venta=int(empleado),fecha_venta__range=(fechainicial_real,fechafinal_real )).values('month','vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('month') #este y funciona con las horas
                if not ventas_vendedor:
                    ventas_vendedor = qs.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1,fecha_venta__range=(fechainicial_real,fechafinal_real)).values('month','vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('month') #este y funciona con las horas
            else:
                ventas_vendedor = Venta.objects.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1,vendedor_venta=int(empleado),fecha_venta__range=(fechainicial_real, fechafinal_real)).values('vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')
                if not ventas_vendedor:
                    ventas_vendedor = Venta.objects.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1,fecha_venta__range=(fechainicial_real, fechafinal_real)).values('vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')

        reporte1=VentasTabla(ventas_vendedor)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteVentas.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_vendedor':form_vendedor,'form_check':form_check})
    else:
        form_fecha=Form_Busqueda_Fechas()
        form_vendedor=Form_Busqueda_Vendedor()
        form_check=Form_Busqueda_Checbox()
        consulta=ventas_vendedor = Venta.objects.filter(entregada_venta=1,es_cotizacion=0,estado_venta=1).values('vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')
        reporte1=VentasTabla(consulta)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteVentas.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_vendedor':form_vendedor,'form_check':form_check})
