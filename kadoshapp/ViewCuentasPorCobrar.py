from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formCuentasPorCobrar import *
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.db.models import Q,F,ExpressionWrapper,FloatField,Sum #para poder usar el operador | que funciona como OR
from datetime import timedelta
#from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
import pytz #para usar la zona horaria
import datetime #para que se pueda dar formato a la fecha

def not_in_Caja_group(user):
    if user:
        return user.groups.filter(name='Caja').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def Abonos(request):
    if request.method=='POST':
        form_busquedas=Form_Abonos_busquedas()
        form_Venta=Form_Abonos_Venta()
        form_Cliente=Form_Abonos_Cliente()
        form_persona=Form_Abonos_Persona()
        form_PCC=Form_Abonos_PagosCuentasPorCobrar()
        form_DetalleVenta=Form_Abonos_DetalleVenta()
        return render(request, 'kadoshapp/Abonos.html', {'form_DetalleVenta':form_DetalleVenta,'form_persona':form_persona,  'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_busquedas':form_busquedas,'form_PCC':form_PCC })
    else:
        form_busquedas=Form_Abonos_busquedas()
        form_Venta=Form_Abonos_Venta()
        form_Cliente=Form_Abonos_Cliente()
        form_persona=Form_Abonos_Persona()
        form_PCC=Form_Abonos_PagosCuentasPorCobrar()
        form_DetalleVenta=Form_Abonos_DetalleVenta()
        return render(request, 'kadoshapp/Abonos.html', {'form_DetalleVenta':form_DetalleVenta,'form_persona':form_persona,  'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_busquedas':form_busquedas,'form_PCC':form_PCC })
