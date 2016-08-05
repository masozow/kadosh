from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q #para poder usar el operador | que funciona como OR


from .models import *
from .formPuntodeVenta import *
#Vista de Punto de Venta
def PuntoDeVenta(request):
    if request.method=='POST':
        #form_Venta=Form_PuntoVenta_Venta(request.POST)
        #if form_Venta.is_valid():
        #    ultima_venta=form_Venta.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Venta=Form_PuntoVenta_Venta()
        form_DetalleVenta=Form_PuntoVenta_DetalleVenta()
        form_InventarioProducto=Form_PuntoVenta_InventarioProducto()
        form_Producto=Form_PuntoVenta_Producto()
        form_TipoProducto=Form_PuntoVenta_TipoProducto()
        form_Promocion=Form_PuntoVenta_Promocion()
        form_Precio=Form_PuntoVenta_Precio()
        form_cliente=Form_PuntoVenta_busquedas()
        form_estiloproducto=Form_PuntoVenta_EstiloProducto()
        form_promocionhasproducto=Form_PuntoVenta_PromocionHasProducto()
        #form_bodega=Form_PuntoVenta_Bodega()
    return render(request, 'kadoshapp/PuntoDeVenta.html', {
                    'form_Venta': form_Venta,
                    'form_DetalleVenta':form_DetalleVenta,
                    'form_TipoProducto':form_TipoProducto,
                    'form_Producto':form_Producto ,
                    'form_InventarioProducto':form_InventarioProducto,
                    'form_Promocion':form_Promocion,
                    'form_Precio':form_Precio,
                    'form_cliente':form_cliente,
                    'form_estiloproducto':form_estiloproducto,
                    'form_promocionhasproducto': form_promocionhasproducto
                    #'form_bodega': form_bodega
                    })


#Vista para obtener solo el producto mediante Ajax
def BuscarProducto(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigobarras_producto') #aquí llamar por el nombre del objeto (name), no por el id
        id_bodega_que_vende = request.POST.get('bodega_idbodega') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
        #runeval(txt_codigo_producto) #se supone que evalua la variable y la envia al debugger
        #pdb.set_trace()  #estos son los breakpoints de django

        response_data = {} #declarando un diccionario vacio
        resp_producto=Producto.objects.filter(codigobarras_producto=txt_codigo_producto)
        #if id_bodega_que_vende is not None:
        #response_data['recibido']=id_bodega_que_vende
        resp_inventario=InventarioProducto.objects.filter(producto_codigo_producto__in=resp_producto,bodega_idbodega=id_bodega_que_vende).order_by('-idinventario_producto')[:1]
        resp_precio=Precio.objects.filter(producto_codigo_producto__in=resp_producto,estado_precio=1).order_by('-idprecio')[:1] #
        response_data['inventario']=serializers.serialize('json', list(resp_inventario), fields=('pk'))
        response_data['nombre']=serializers.serialize('json', list(resp_producto), fields=('nombre_producto'))
        response_data['valorprod']=serializers.serialize('json', list(resp_precio), fields=('valor_precio'))
        #if not id_bodega_que_vende:

        #    if resp_producto.exists() and resp_inventario.exists() and resp_precio.exists():

        #__in sirve para indicar que ese campo debe ser buscado dentro del objeto al que se hace referencia

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def BuscarProductoCaracteristicas(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigo_estilo_producto') #aquí llamar por el nombre del objeto (name), no por el id

        id_bodega_que_vende = request.POST.get('bodega_idbodega') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
        if not id_bodega_que_vende:
            id_bodega_que_vende=0

        id_marca_producto = request.POST.get('marca_producto')
        if not id_marca_producto:
            id_marca_producto=0

        id_estilo_producto = request.POST.get('estilo_producto')
        if not id_estilo_producto:
            id_estilo_producto=0

        id_tipo_producto = request.POST.get('tipo_producto')
        if not id_tipo_producto:
            id_tipo_producto=0

        id_talla_producto = request.POST.get('talla_producto')
        if not id_talla_producto:
            id_talla_producto=0

        id_color_producto = request.POST.get('color_producto')
        if not id_color_producto:
            id_color_producto=0

        id_genero_producto = request.POST.get('genero_producto')
        if not id_genero_producto:
            id_genero_producto=0

        #runeval(txt_codigo_producto) #se supone que evalua la variable y la envia al debugger
        #pdb.set_trace()  #estos son los breakpoints de django

        response_data = {} #declarando un diccionario vacio
        response_data['codigo_producto']=txt_codigo_producto
        response_data['bodega_producto']=id_bodega_que_vende
        response_data['marca_producto']=id_marca_producto
        response_data['estilo_producto']=id_estilo_producto
        response_data['tipo_producto']=id_tipo_producto
        response_data['talla_producto']=id_talla_producto
        response_data['color_producto']=id_color_producto
        response_data['genero_producto']=id_genero_producto
        #La Q en el siguiente queryset es importantisima, sin ella no funciona los OR, representados por el poerador |
        resp_producto=Producto.objects.filter(Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto))
        resp_inventario=InventarioProducto.objects.filter(producto_codigo_producto__in=resp_producto,bodega_idbodega=id_bodega_que_vende).order_by('-idinventario_producto')[:1]
            #__in sirve para indicar que ese campo debe ser buscado dentro del objeto al que se hace referencia
        resp_precio=Precio.objects.filter(producto_codigo_producto__in=resp_producto,estado_precio=1).order_by('-idprecio')[:1] #
        resp_foto=
        response_data['inventario']=serializers.serialize('json', list(resp_inventario), fields=('pk'))
        response_data['producto']=serializers.serialize('json', list(resp_producto))
        response_data['valorprod']=serializers.serialize('json', list(resp_precio), fields=('valor_precio'))

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
