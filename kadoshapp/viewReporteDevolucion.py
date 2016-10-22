from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum #para poder hacer la suma de los campos
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from .formReporteDevolucion import *
from datetime import datetime,timedelta
import pytz #para poder hacer la suma de los campos

def not_in_AdministradorSistema_group(user):
    if user:
        return user.groups.filter(name='AdministradorSistema').count() != 0
    return False

@login_required
@user_passes_test(not_in_AdministradorSistema_group, login_url='denegado')
def devolucion(request):
    if request.method == 'POST':
        form_devolucion=Form_RepDevolucion_Devolucion(request.POST)
        fecha1= request.POST.get('fechainicial')
        fecha2= request.POST.get('fechafinal')

        if fecha1:
            fechasplit1=str(fecha1).split('/')
            dia=fechasplit1[0]
            mes=fechasplit1[1]
            anio=fechasplit1[2]
            fecha1=datetime(int(anio),int(mes), int(dia),0,0,0,tzinfo=pytz.UTC)
            fecha1=fecha1+timedelta(hours=6)
        if fecha2:
            fechasplit2=str(fecha2).split('/')
            dia=fechasplit2[0]
            mes=fechasplit2[1]
            anio=fechasplit2[2]
            fecha2=datetime(int(anio),int(mes), int(dia),23,59,59,tzinfo=pytz.UTC)
            fecha2=fecha2+timedelta(hours=6)

        if not fecha1 and not fecha2:
            resultado_devolucion=Devolucion.objects.all()
        else:
		   #Cuando existe por lo menos un parámetro (los números dentro de filter deben reemplazarse por los parámetros que envía el usuario)
           resultado_devolucion=Devolucion.objects.filter(momento_devolucion__range=(fecha1,fecha2))
        reporte1=DevolucionTabla(resultado_devolucion)
        RequestConfig(request).configure(reporte1)
        return render(request,'kadoshapp/ReporteDevolucion.html',{'reporte1':reporte1,'form_devolucion':form_devolucion})
    else:
        form_devolucion=Form_RepDevolucion_Devolucion()
        resultado_devolucion=Devolucion.objects.all()
        reporte1=DevolucionTabla(resultado_devolucion)
        #RequestConfig(request).configure(reporte1)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteDevolucion.html',{'reporte1':reporte1,'form_devolucion':form_devolucion})
