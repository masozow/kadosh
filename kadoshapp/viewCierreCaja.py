from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import *
from .formCierreCaja import *

#vista CierreDeCaja
@login_required
def CierreDeCaja(request):
    if request.method=='POST':
        form_Cierrecaja=Form_CierreDeCaj_CierreDeCaja(request.POST)
        if form_Cierrecaja.is_valid():
            ultimo_cierre=form_Cierrecaja.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Cierrecaja=Form_CierreDeCaj_CierreDeCaja()
        form_empleado=Form_CierreDeCaj_Empleado()

    return render(request, 'kadoshapp/CierreDeCaja.html', {'form_Cierrecaja':form_Cierrecaja,'form_empleado':form_empleado })
