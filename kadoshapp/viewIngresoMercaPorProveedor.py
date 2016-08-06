from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *
from .formIngresoMercaPorProveedor import *

#Vista de formulario de IngresoDeMercaderiaPorProveedor
def ingresodemercaderiaporProveedor(request):
    if request.method=='POST':
        form_Producto=Form_IngresoMercaderiaPorProveedor_Producto(request.POST)
        if form_Producto.is_valid():
            ultimo_producto=form_Producto.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Producto=Form_IngresoMercaderiaPorProveedor_Producto()
        form_Detallecompra=Form_IngresoMercaderiaPorProveedor_DetalleCompra()
        form_TipoProducto=Form_IngresoMercaderiaPorProveedor_TipoProducto()
        form_fotografia=Form_IngresoMercaderiaPorProveedor_Fotografia()
        form_InventarioProducto=Form_IngresoMercaderiaPorProveedor_InventarioProducto()
        #form_anaquel=Form_IngresoMercaderiaPorProveedor_Anaquel()
        form_Compra=Form_IngresoMercaderiaPorProveedor_Compra()
    return render(request, 'kadoshapp/IngresoMercaderiaPorProveedor.html', {'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto,  'form_Compra':form_Compra })
