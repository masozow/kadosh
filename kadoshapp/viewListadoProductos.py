from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formListadoProductos import *

def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado')
def Listado(request):
    if request.method=='POST':
        form_prducto=Form_Busqueda_Listado_Precio(request.POST)
        if form_prducto.is_valid():
            ultima_busqueda=form_producto.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_producto=Form_Listado_Producto()

    return render(request, 'kadoshapp/ListadoProductos.html', {'form_producto':form_producto })

@login_required
def BuscarProductoExtra(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigobarras_producto')
        #runeval(txt_codigo_producto) #se supone que evalua la variable y la envia al debugger
        #pdb.set_trace()  #estos son los breakpoints de django

        response_data = {} #declarando un diccionario vacio
        #resultado=Producto.objects.filter(codigobarras_producto=123,inventarioproducto__detallecompra_pk=DetalleCompra.objects.filter(pk=F(inventarioproducto__detallecompra__pk)).order_by(pk)[:1]).values('pk','nombre_producto','inventarioproducto__bodega_idbodega__nombre_bodega','codigobarras_producto','inventarioproducto__existencia_actual','codigoestilo_producto','precio__valor_precio',F('inventarioproducto__detallecompra__valor_parcial_compra')/F('inventarioproducto__detallecompra__valor_cantidad_compra')).order_by('-inventarioproducto__detallecompra__pk')

        resultado=Producto.objects.filter(codigobarras_producto=123).values('pk',
                                                                            'nombre_producto',
                                                                            'inventarioproducto__bodega_idbodega__nombre_bodega',
                                                                            'codigobarras_producto',
                                                                            'inventarioproducto__existencia_actual',
                                                                            'codigoestilo_producto',
                                                                            'precio__valor_precio'  #        F(inventarioproducto__detallecompra__valor_parcial_compra)
                                                                            ).order_by('-inventarioproducto__detallecompra__pk')
        resp_producto=Producto.objects.filter(codigobarras_producto=txt_codigo_producto)
        #if id_bodega_que_vende is not None:
        #response_data['recibido']=id_bodega_que_vende
        resp_inventario=InventarioProducto.objects.filter(producto_codigo_producto__in=resp_producto,bodega_idbodega=id_bodega_que_vende).order_by('-idinventario_producto')[:1]
        resp_precio=Precio.objects.filter(producto_codigo_producto__in=resp_producto,estado_precio=1).order_by('-idprecio')[:1] #
        #Cod 	Producto 	Sucursal 	Bodega 	Codigo Barras 	Existencia 	Codigo estilo 	Costo 	Precio

        response_data['inventario']=serializers.serialize('json', list(resp_inventario), fields=('pk'))
        response_data['nombre']=serializers.serialize('json', list(resp_producto), fields=('nombre_producto'))
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

@login_required
def BuscarProductoCaracteristicasExtra(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigo_estilo_producto')

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

        response_data = {} #declarando un diccionario vacio
        #La Q en el siguiente queryset es importantisima, sin ella no funciona los OR, representados por el poerador |
        #resp_producto=Producto.objects.filter(Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto))
        resp_consulta=consulta_sql_personalizada(id_bodega_que_vende,txt_codigo_producto,id_marca_producto,id_tipo_producto,id_estilo_producto,id_talla_producto,id_color_producto,id_genero_producto)
        #A continuacion se usa una consulta SQL comun y corriente, prestar atencion al placeholder "%s" que es para un valor unico, y al parametro con el formato values_list('un_campo',flat=True), que hace que se envie un solo valor del resultado de ese queryset
        #resp_foto=Fotografia.objects.raw('SELECT F.idfotografia,F.ruta_fotografia FROM Fotografia as F INNER JOIN Producto_has_Fotografia as PF on F.idfotografia=PF.fotografia_idfotografia WHERE PF.producto_codigo_producto=%s AND F.principal_fotografia=1',resp_producto.values_list('codigo_producto',flat=True))
        response_data['consulta']=resp_consulta

        return HttpResponse(
            json.dumps(response_data,default=default),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
