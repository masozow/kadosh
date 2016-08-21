from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from .models import *
from .formcompra import *
from django.db.models import Q #para poder usar el operador | que funciona como OR

#se define a que grupo no permitir acceso
def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

@login_required
#linea para no permitir acceso al grupo
@user_passes_test(not_in_Bodega_group, login_url='denegado')
#Vista de form de compra
def Compra(request):
    if request.method=='POST':
        form_Compra=Form_Compra_Compra(request.POST)
        form_Proveedor=Form_Compra_Proveedor
        form_Detallecompra=Form_Compra_DetalleCompra(request.POST)
        form_InventarioProducto=Form_Compra_InventarioProducto(request.POST)
        form_Producto=Form_Compra_Producto(request.POST)
        form_fotografia=Form_Compra_Fotografia(request.POST)
        form_tabla=FormTabla(request.POST)
        #if form_Compra.is_valid():
        #    ultima_Compra=form_Compra.save()
        return render(request, 'kadoshapp/Compra.html', {'form_Proveedor':form_Proveedor, 'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto, 'form_Compra':form_Compra,'form_tabla':form_tabla })
    else:
        form_Compra=Form_Compra_Compra()
        form_Proveedor=Form_Compra_Proveedor
        form_Detallecompra=Form_Compra_DetalleCompra()
        form_InventarioProducto=Form_Compra_InventarioProducto()
        form_Producto=Form_Compra_Producto()
        form_fotografia=Form_Compra_Fotografia()
        form_tabla=FormTabla()
        #form_anaquel=Form_Compra_Anaquel()
        form_TipoProducto=Form_Compra_TipoProducto()
    return render(request, 'kadoshapp/Compra.html', {'form_Proveedor':form_Proveedor, 'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto, 'form_Compra':form_Compra,'form_tabla':form_tabla })


def SubirImagen(request):
    if request.method == 'POST':
        fotografia = Form_Compra_Fotografia(data=request.POST, files=request.FILES)
        response_data={}
        if fotografia.is_valid():
            foto=fotografia.save(commit=False)
            foto.principal_fotografia=True
            #foto.save()
            #response_data['idfoto']=foto.pk
        else:
            response_data['error']='imagen no válida'
        producto=Form_Compra_Producto(request.POST)
        if producto.is_valid():
            datosproducto=producto.cleaned_data
            codigobarras=datosproducto['codigobarras_producto']
            codigoestilo=datosproducto['codigoestilo_producto']
            nombreproducto=datosproducto['nombre_producto']
            tipoproducto=datosproducto['tipo_producto_idtipo_producto']
            estiloproducto=datosproducto['estilo_idestilo']
            marcaproducto=datosproducto['marca_id_marca']
            colorproducto=datosproducto['color_idcolor']
            tallaproducto=datosproducto['talla_idtalla']
            generoproducto=datosproducto['genero_idgener']
            prod1=Producto.objects.filter(Q(codigobarras_producto=codigobarras)|Q(codigoestilo_producto=codigoestilo)).values('pk')
            if not prod1:
                prod1=Producto.objects.filter(marca_id_marca=marcaproducto,estilo_idestilo=estiloproducto,tipo_producto_idtipo_producto=tipoproducto,genero_idgener=generoproducto,color_idcolor=colorproducto,talla_idtalla=tallaproducto)
                if not prod1:
                    prod1=producto.save(commit=False)

            response_data['producto']=ValuesQuerySetToDict(prod1)
        return HttpResponse(
            json.dumps(response_data,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

#if request.is_ajax():
#    form_fotografia=Form_Compra_Fotografia(request.POST)
#    name = request.POST.get('name')
#    description = request.POST.get('description')
#    icon = request.FILES.get('icon')
#    article_new = Article(
#        name=name,
#        description=description,
#        icon=icon
#    )
#    article_new.save()
