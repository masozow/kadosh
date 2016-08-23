from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formProductos import *


@login_required
def CosasProducto(request):
    if request.method=='POST':
        form_color=Form_Producto_Color(request.POST)
        form_estilo=Form_Producto_Estilo(request.POST)
        form_genero=Form_Producto_Genero(request.POST)
        form_marca=Form_Producto_Marca(request.POST)
        form_talla=Form_Producto_Talla(request.POST)
        form_tipo=Form_Producto_Tipo(request.POST)

        if form_color.is_valid():
            datoscolor=form_color.cleaned_data
            if not Color.objects.get(nombre_color=datoscolor['nombre_color']):
                form_color.save()
                form_color=Form_Producto_Color()
        if form_estilo.is_valid():
            datosestilo=form_estilo.cleaned_data
            if not Estilo.objects.get(nombre_estilo=datosestilo['nombre_estilo']):
                form_estilo.save()
                form_estilo=Form_Producto_Estilo()
        if form_genero.is_valid():
            datosgenero=form_genero.cleaned_data
            if not Genero.objects.get(nombre_genero=datosgenero['nombre_genero']):
                form_genero.save()
                form_genero=Form_Producto_Genero()
        if form_marca.is_valid():
            datosmarca=form_marca.cleaned_data
            if not Marca.objects.get(nombre_marca=datosmarca['nombre_marca']):
                form_marca.save()
                form_marca=Form_Producto_Marca()
        if form_talla.is_valid():
            datostalla=form_talla.cleaned_data
            if not Talla.objects.get(nombre_talla=datostalla['nombre_talla']):
                form_talla.save()
                form_talla=Form_Producto_Talla()
        if form_tipo.is_valid():
            datostipo=form_tipo.cleaned_data
            if not TipoProducto.objects.get(nombre_tipoproducto=datostipo['nombre_tipoproducto']):
                form_tipo.save()
                form_tipo=Form_Producto_Tipo()

        return render(request, 'kadoshapp/ElementoProducto.html', {'form_color':form_color,'form_estilo':form_estilo,'form_genero':form_genero,'form_marca':form_marca,'form_talla':form_talla,'form_tipo':form_tipo })
    else:
        form_color=Form_Producto_Color()
        form_estilo=Form_Producto_Estilo()
        form_genero=Form_Producto_Genero()
        form_marca=Form_Producto_Marca()
        form_talla=Form_Producto_Talla()
        form_tipo=Form_Producto_Tipo()
    return render(request, 'kadoshapp/ElementoProducto.html', {'form_color':form_color,'form_estilo':form_estilo,'form_genero':form_genero,'form_marca':form_marca,'form_talla':form_talla,'form_tipo':form_tipo })
