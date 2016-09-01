from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum #para poder hacer la suma de los campos
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from .formReporteCierreCaja import *
from datetime import datetime

def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado') #linea para no permitir acceso al grupo
def cierre_caja(request):
    if request.method == 'POST':
        form_cierre=Form_RepCierreCaja_CierreDeCaja(request.POST)
        caja=request.POST.get('caja_idcaja')
        fecha= request.POST.get('fecha_cierredecaja')
        if fecha:
            fechasplit=str(fecha).split('/')
            dia=fechasplit[0]
            mes=fechasplit[1]
            anio=fechasplit[2]
            fecha=anio+'-'+mes+'-'+dia
         #el not indica que la cadena está vacía, o que la variable es null
        if not caja:
            caja=0

        if not caja and not fecha:
            resultado_cierre=CierreDeCaja.objects.all()
        else:
		   #Cuando existe por lo menos un parámetro (los números dentro de filter deben reemplazarse por los parámetros que envía el usuario)
            resultado_cierre=CierreDeCaja.objects.filter(Q(caja_idcaja=caja)|Q(fecha_cierredecaja=fecha))
        reporte1=CierreTabla(resultado_cierre)
        RequestConfig(request).configure(reporte1)
        return render(request,'kadoshapp/ReporteCierreCaja.html',{'reporte1':reporte1,'form_cierre':form_cierre})
    else:
        form_cierre=Form_RepCierreCaja_CierreDeCaja()
        resultado_cierre=CierreDeCaja.objects.all()
        reporte1=CierreTabla(resultado_cierre)
        #RequestConfig(request).configure(reporte1)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteCierreCaja.html',{'reporte1':reporte1,'form_cierre':form_cierre})
