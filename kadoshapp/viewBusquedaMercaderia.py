from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formBusquedaMercaderia import *
def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado')
def BusquedaMerca(request):
    if request.method=='POST':
        form_prducto=Form_Busqueda_Producto_Precio(request.POST)
        if form_precio.is_valid():
            ultima_busqueda=form_producto.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_producto=Form_Busqueda_Producto()

    return render(request, 'kadoshapp/BusquedaMercaderia.html', {'form_producto':form_producto })
