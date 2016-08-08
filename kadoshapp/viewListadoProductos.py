from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formListadoProductos import *

@login_required
def Listado(request):
    if request.method=='POST':
        form_prducto=Form_Busqueda_Listado_Precio(request.POST)
        if form_prducto.is_valid():
            ultima_busqueda=form_producto.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_producto=Form_Listado_Producto()

    return render(request, 'kadoshapp/ListadoProductos.html', {'form_producto':form_producto })
