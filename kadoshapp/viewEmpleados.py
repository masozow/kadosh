from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *
from .formEmpleados import *

def Empleados(request):
    if request.method=='POST':
        form_empleado=Form_Empleados_Empleado(request.POST)
        if form_empleados.is_valid():
            ultimo_empleado=form_empleado.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
        else:
            form_empleado=Form_Empleados_Empleado()
            form_persona=Form_Empleados_Persona()

        return render(request, 'kadoshapp/AnularVenta.html', {'form_persona':form_persona,  'form_empleado':form_empleado })
