from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formAsignarCaja import *
@login_required
def Asignacion(request):
    if request.method=='POST':
        form_caja=Form_Asignar_CajaHasEmpleado(request.POST)
        if form_caja.is_valid():
            asignacion=form_caja.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_caja=Form_Asignar_CajaHasEmpleado()

    return render(request, 'kadoshapp/AsignarCaja.html', {'form_caja':form_caja })
