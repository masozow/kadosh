from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum #para poder hacer la suma de los campos
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from .formReporteGastos import *
from datetime import timedelta
import datetime
import pytz

def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado') #linea para no permitir acceso al grupo
def gastos(request):
    if request.method == 'POST':
        form_gastos=Form_RepGastos_Gastos(request.POST)
        caja=request.POST.get('caja_idcaja')
        fecha= request.POST.get('momento_gasto')
        if fecha:
            fecha1_split=str(fecha).split('/')
            fechainicial_real=datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),0,0,0,tzinfo=pytz.UTC)
            fechafinal_real=datetime.datetime(int(fecha1_split[2]),int(fecha1_split[1]), int(fecha1_split[0]),23,59,59,tzinfo=pytz.UTC)
            fechainicial_real=fechainicial_real+datetime.timedelta(hours=6)
            fechafinal_real=fechafinal_real+datetime.timedelta(hours=6)
         #el not indica que la cadena está vacía, o que la variable es null
        if not caja:
            caja=0

        if not fecha:
            resultado_gastos=Gastos.objects.filter(caja_idcaja=caja)
        else:
            if caja:
                resultado_gastos=Gastos.objects.filter(caja_idcaja=caja,momento_gasto__range=(fechainicial_real,fechafinal_real))
            elif fecha:
                resultado_gastos=Gastos.objects.filter(momento_gasto__range=(fechainicial_real,fechafinal_real))
            else:
                resultado_gastos=Gastos.objects.all()


        #if not caja and not fecha:
        #    resultado_gastos=Gastos.objects.all()
        #else:
		   #Cuando existe por lo menos un parámetro (los números dentro de filter deben reemplazarse por los parámetros que envía el usuario)
        #    resultado_gastos=Gastos.objects.filter(Q(caja_idcaja=caja)|Q(momento_gasto__range=(fechainicial_real,fechafinal_real)))
        reporte1=GastosTabla(resultado_gastos)
        RequestConfig(request).configure(reporte1)
        return render(request,'kadoshapp/ReporteGastos.html',{'reporte1':reporte1,'form_gastos':form_gastos})
    else:
        form_gastos=Form_RepGastos_Gastos()
        resultado_gastos=Gastos.objects.all()
        reporte1=GastosTabla(resultado_gastos)
        RequestConfig(request).configure(reporte1)
        return render(request,'kadoshapp/ReporteGastos.html',{'reporte1':reporte1,'form_gastos':form_gastos})
