from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *
from .formAnularVenta import *
#vista Anular Venta
def AnularVenta(request):
    if request.method=='POST':
        form_Venta=Form_AnulaVenta_Venta(request.POST)
        if form_Venta.is_valid():
            ultima_anulacionventa=form_Venta.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Venta=Form_AnulaVenta_Venta()
        form_Cliente=Form_AnulaVenta_Cliente()
        form_DetalleVenta=Form_AnulaVenta_DetalleVenta()
        form_empleado=Form_AnulaVenta_Empleado()
        form_persona=Form_AnulaVenta_Persona()
    return render(request, 'kadoshapp/AnularVenta.html', {'form_persona':form_persona,  'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_DetalleVenta':form_DetalleVenta, 'form_empleado':form_empleado })
