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

        return render(request, 'kadoshapp/ingres_mercaderia.html', { })
    else:
        form_color=Form_Producto_Color()
        form_estilo=Form_Producto_Estilo()
        form_genero=Form_Producto_Genero()
        form_marca=Form_Producto_Marca()
        form_talla=Form_Producto_Talla()
        form_tipo=Form_Producto_Tipo()
    return render(request, 'kadoshapp/ElementoProducto.html', {'form_color':form_color,'form_estilo':form_estilo,'form_genero':form_genero,'form_marca':form_marca,'form_talla':form_talla,'form_tipo':form_tipo })
