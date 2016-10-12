from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
import pytz
import datetime #para que se pueda dar formato a la fecha
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formCierreCaja import *
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin ca
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.db.models import Sum #para poder hacer la suma de los campos
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

def not_in_Caja_group(user):
    if user:
        return user.groups.filter(name='Caja').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

#vista CierreDeCaja
@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def CierreDeCaja(request):
    if request.method=='POST':
        form_Cierrecaja=Form_CierreDeCaj_CierreDeCaja(request.POST) #se obtiene el formulario que vino con el request
        form_empleado=Form_CierreDeCaj_Empleado(request.POST)#se obtiene el formulario que vino con el request
        if form_Cierrecaja.is_valid(): #se comprueba que el formulario sea válido, es decir, que cumpla con las restricciones descritas en el model
            if form_empleado.is_valid(): #se comprueba que el formulario sea válido, es decir, que cumpla con las restricciones descritas en el model
                datosempleado=form_empleado.cleaned_data #se obtienen los datos que venían dentro de los elementos del formulario
                if datosempleado['codigo_autorizacion_empleado']: #si el codigo de autorización contiene por lo menos un dato
                    codigo=datosempleado['codigo_autorizacion_empleado'] #se obtiene el código escrito por el usuario
                    cierre=form_Cierrecaja.cleaned_data #se obtienen los datos que venían dentro de los elementos del formulario
                    empleadoautorizo=cierre['empleado_idempleado'] #se obtiene el empleado elegido en el selectinput/combobox, este es un objeto Empleado no un código como tal, esto ocurre porque esa es una llave foránea
                    empleado=Empleado.objects.filter(codigo_autorizacion_empleado=codigo,pk=empleadoautorizo.pk) #se busca el empleado que tena ese código y esa llave primaria (pk)
                    if empleado: #si existe un empleado con las dos restricciones anteriores
                        guardarcierre=form_Cierrecaja.save() #se guarda el cierre de caja con todos los datos escritos por el usuario
                        form_Cierrecaja=Form_CierreDeCaj_CierreDeCaja() #se obtiene un formulario limpio
                        form_empleado=Form_CierreDeCaj_Empleado() #se obtiene un formulario limpio
                        form_Cierrecaja.fields["empleado_idempleado"].queryset = Empleado.objects.filter(estado_empleado=1)
        return render(request, 'kadoshapp/CierreDeCaja.html',{'form_Cierrecaja':form_Cierrecaja,'form_empleado':form_empleado })
    else:
        form_Cierrecaja=Form_CierreDeCaj_CierreDeCaja()
        form_empleado=Form_CierreDeCaj_Empleado()
        form_Cierrecaja.fields["empleado_idempleado"].queryset = Empleado.objects.filter(estado_empleado=1)
    return render(request, 'kadoshapp/CierreDeCaja.html', {'form_Cierrecaja':form_Cierrecaja,'form_empleado':form_empleado })

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def BuscarCaja(request):
    if request.method == 'POST':
        caja = request.POST.get('caja')

        if not caja:
            caja=0
        response_data={}
        #hoy_min = datetime.datetime.combine(timezone.now(), datetime.time.min) #,tzinfo=pytz.UTC
        #hoy_min=hoy_min+timedelta(hours=6)
        #hoy_max = datetime.datetime.combine(timezone.now(), datetime.time.max) #,tzinfo=pytz.UTC
        #hoy_max=hoy_max+timedelta(hours=6)
        #hoy_min=pytz.utc.localize(hoy_min)
        #hoy_max=pytz.utc.localize(hoy_max))=
        hoy_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min) #.replace(tzinfo=timezone.UTC())).astimezone(pytz.timezone('America/Guatemala'))
        hoy_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max) #.replace(tzinfo=timezone.UTC())).astimezone(pytz.timezone('America/Guatemala'))
        hoy_min=pytz.utc.localize(hoy_min)
        hoy_max=pytz.utc.localize(hoy_max)
        hoy_max=hoy_max+timedelta(hours=6)
        hoy_min=hoy_min+timedelta(hours=6)
        gastos=Gastos.objects.filter(caja_idcaja=int(caja),momento_gasto__range=(hoy_min,hoy_max)).values('caja_idcaja__pk').annotate(total_gastos=Sum('monto_gasto'))
        efectivo=Venta.objects.filter(estado_venta=1,es_cotizacion=0,tipo_pago_idtipo_pago=TipoPago(pk=1),fecha_venta__range=(hoy_min,hoy_max),caja_idcaja=Caja(pk=caja)).values('caja_idcaja__pk').annotate(total_efectivo=Sum('total_venta'))
        tarjeta=Venta.objects.filter(estado_venta=1,es_cotizacion=0,tipo_pago_idtipo_pago=TipoPago(pk=3),fecha_venta__range=(hoy_min,hoy_max),caja_idcaja=Caja(pk=caja)).values('caja_idcaja__pk').annotate(total_tarjeta=Sum('total_venta'))
        cheque=Venta.objects.filter(estado_venta=1,es_cotizacion=0,tipo_pago_idtipo_pago=TipoPago(pk=2),fecha_venta__range=(hoy_min,hoy_max),caja_idcaja=Caja(pk=caja)).values('caja_idcaja__pk').annotate(total_cheque=Sum('total_venta'))
        gastos_dic=ValuesQuerySetToDict(gastos)
        efectivo_dic=ValuesQuerySetToDict(efectivo)
        tarjeta_dic=ValuesQuerySetToDict(tarjeta)
        cheque_dic=ValuesQuerySetToDict(cheque)
        response_data['gastos']=gastos_dic
        response_data['efectivo']=efectivo_dic#serializers.serialize('json', list(efectivo))
        response_data['tarjeta']=tarjeta_dic#serializers.serialize('json', list(tarjeta))
        response_data['cheque']=cheque_dic#serializers.serialize('json', list(cheque))
        #ingresos=
        return HttpResponse(
            json.dumps(response_data,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
