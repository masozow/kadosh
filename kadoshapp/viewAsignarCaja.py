from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formAsignarCaja import *

def not_in_Supervisor_group(user):
    if user:
        return user.groups.filter(name='Supervisor').count() != 0
    return False

@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def RegistrarGasto(request):
    if request.method=='POST':
        form_gasto=Form_Gastos(request.POST)
        if form_gasto.is_valid():
            gasto=form_gasto.save()
            form_gasto=Form_Gastos()
        return render(request, 'kadoshapp/AsignarCaja.html', {'form_gasto':form_gasto })
    else:
        form_gasto=Form_Gastos(request.POST)
    return render(request, 'kadoshapp/AsignarCaja.html', {'form_gasto':form_gasto })
