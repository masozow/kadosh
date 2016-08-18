from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formPromocion import *

#se define a que grupo no permitir acceso
def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

#Vista de Promocion
@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado')
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
        form_producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
    return render(request, 'kadoshapp/Promocion.html', {'form_precio':form_precio,'form_promocion':form_promocion, 'form_producto':form_producto, 'form_tipoproducto':form_tipoproducto, 'form_inventarioproducto':form_inventarioproducto , 'form_cantidad':form_cantidad  })
