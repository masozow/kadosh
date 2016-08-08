from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .formPromocion import *
#Vista de Promocion
@login_required
def Promocion(request):
    if request.method=='POST':
        form_promocion=Form_Promocion_Promocion(request.POST)
        if form_promocion.is_valid():
            ultima_promocion=form_promocion.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_promocion=Form_Promocion_Promocion()
        form_producto=Form_Promocion_Producto()
        form_tipoproducto=form_Promocion_TipoProducto()
        form_inventarioproducto=Form_Promocion_InventarioProducto()
        form_cantidad=form_Promocion_Cantidad()
        form_precio=Form_Promocion_Precio()
    return render(request, 'kadoshapp/Promocion.html', {'form_precio':form_precio,'form_promocion':form_promocion, 'form_producto':form_producto, 'form_tipoproducto':form_tipoproducto, 'form_inventarioproducto':form_inventarioproducto , 'form_cantidad':form_cantidad  })
