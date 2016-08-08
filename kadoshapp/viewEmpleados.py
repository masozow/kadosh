from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import *
from .formEmpleados import *
@login_required
def Empleados(request):
    if request.method=='POST':
        form_estandares=Form_Empleados_Estandares(request.POST)
        if form_empleados.is_valid():
            ultima_categoria=form_estandares.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_empleado=Form_Empleados_Empleado()
        form_persona=Form_Empleados_Persona()
        form_estandares=Form_Empleados_Estandares()
    return render(request, 'kadoshapp/Empleados.html', {'form_estandares':form_estandares,'form_persona':form_persona,  'form_empleado':form_empleado })
