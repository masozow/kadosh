from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formPrecios import *
def not_in_Supervisor_group(user):
    if user:
        return user.groups.filter(name='Supervisor').count() != 0
    return False

@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def Precios(request):
    if request.method=='POST':
        form_precio=Form_Precios_Precio(request.POST)
        if form_precio.is_valid():
            ultimo_precios=form_precio.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_producto=Form_Precios_Producto()
        form_precio=Form_Precios_Precio()
        form_InventarioProducto=Form_Precios_InventarioProducto
    return render(request, 'kadoshapp/Precios.html', {'form_InventarioProducto':form_InventarioProducto,'form_precio':form_precio,  'form_producto':form_producto })
