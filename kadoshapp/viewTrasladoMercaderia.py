from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formTrasladoMercaderia import *
def not_in_Traslado_group(user):
    if user:
        return user.groups.filter(name='Traslado').count() != 0
    return False

#CVista de Traslado de mercaderia
@login_required
@user_passes_test(not_in_Traslado_group, login_url='denegado')
def TrasladoMercaderia(request):
    if request.method=='POST':
        form_Traslado=Form_TrasladoMerca_TrasaladoMercaderia(request.POST)
        if form_Traslado.is_valid():
            ultimo_traslado=form_Traslado.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Traslado=Form_TrasladoMerca_TrasaladoMercaderia()
        form_Producto=Form_TrasladoMerca_Producto
        form_TipoProducto=Form_TrasladoMerca_TipoProducto
        form_InventarioProducto=Form_TrasladoMerca_InventarioProducto
        form_cantidad=Form_TrasladoMerca_Cantidad
    return render(request, 'kadoshapp/TrasladoMerca.html', {'form_TipoProducto':form_TipoProducto,'form_Producto':form_Producto ,'form_InventarioProducto':form_InventarioProducto, 'form_Traslado':form_Traslado, 'form_cantidad':form_cantidad })
