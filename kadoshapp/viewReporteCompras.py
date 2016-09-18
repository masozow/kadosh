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
from .formReporteCompras import *
from datetime import timedelta

def not_in_AdministradorSistema_group(user):
    if user:
        return user.groups.filter(name='AdministradorSistema').count() != 0
    return False

@login_required
@user_passes_test(not_in_AdministradorSistema_group, login_url='denegado')
def Compras(request):
    if request.method == 'POST':
        form_check=Form_Busqueda_Checkbox(request.POST)
        form_fecha=Form_Busqueda_Fechas(request.POST)
        form_vendedor=Form_Busqueda_Vendedor(request.POST)
        fechaini = request.POST.get('fechainicial_precio')
        fechafini = request.POST.get('fechafinal_precio')
        box = request.POST.get('checkbox_vrf', False)
        fecha1=fechaini #debe ser la fecha más pequeña
        fecha2=fechafini #debe ser la fecha más grande
        if fecha1 and fecha2:
            fecha1_split=fecha1.split('/')
            fecha2_split=fecha2.split('/')
            fechainicial_real=datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),0,0,0,tzinfo=pytz.UTC)
            fechafinal_real=datetime.datetime(int(fecha2_split[2]),int(fecha2_split[1]), int(fecha2_split[0]),23,59,59,tzinfo=pytz.UTC)
            fechainicial_real=fechainicial_real+datetime.timedelta(hours=6)
            fechafinal_real=fechafinal_real+datetime.timedelta(hours=6)
            compras=Compra.objects.filter(fecha_realizacion_compra__range=(fechainicial_real,fechafinal_real),vrf_compra=box)
        else:
            compras=Compra.objects.filter(vrf_compra=box)
        reporte1=ComprasTabla(compras)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteCompras.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_vendedor':form_vendedor,'form_check':form_check})
    else:
        form_fecha=Form_Busqueda_Fechas()
        form_vendedor=Form_Busqueda_Vendedor()
        form_check=Form_Busqueda_Checkbox()
        consulta=Compra.objects.all()
        reporte1=ComprasTabla(consulta)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteCompras.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_vendedor':form_vendedor,'form_check':form_check})
