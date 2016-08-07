from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from collections import namedtuple #Sirve en la funcion de tuplas
from decimal import Decimal #para hacer la conversion decimal a JSON


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


def BuscarProductoImagenPrincipal(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigo_producto')
        response_data = {} #declarando un diccionario vacio
        #A continuacion se usa una consulta SQL comun y corriente, prestar atencion al placeholder "%s" que es para un valor unico, y al parametro con el formato values_list('un_campo',flat=True), que hace que se envie un solo valor del resultado de ese queryset
        resp_foto=Fotografia.objects.raw('SELECT F.idfotografia,F.ruta_fotografia FROM Fotografia as F INNER JOIN Producto_has_Fotografia as PF on F.idfotografia=PF.fotografia_idfotografia WHERE PF.producto_codigo_producto=%s AND F.principal_fotografia=1',txt_codigo_producto)[:1]
        #resp_ruta_foto=Fotografia.objects.raw('SELECT F.idfotografia,F.ruta_fotografia FROM Fotografia as F INNER JOIN Producto_has_Fotografia as PF on F.idfotografia=PF.fotografia_idfotografia WHERE PF.producto_codigo_producto=%s AND F.principal_fotografia=1',txt_codigo_producto).url
        response_data['fotografia']=serializers.serialize('json', list(resp_foto))
        #response_data['ruta']=serializers.serialize('json', list(resp_ruta))
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def GuardarVenta(request):
    if request.method == 'POST':
        rec_anotaciones_venta = request.POST.get('env_anotaciones_venta')
        rec_cliente_idcliente = request.POST.get('env_cliente_idcliente')
        rec_tipo_pago_idtipo_pago = request.POST.get('env_tipo_pago_idtipo_pago')
        rec_contado_venta = request.POST.get('env_contado_venta')
        rec_vendedor_venta = request.POST.get('env_vendedor_venta')
        rec_caja_idcaja = request.POST.get('env_caja_idcaja')
        rec_es_cotizacion = request.POST.get('env_es_cotizacion')
        rec_total_venta = request.POST.get('env_total_venta')

        #post = Post(text=post_text, author=request.user)
        #post.save()
        #probar lo siguiente
        #empleado=Empleado.objects.get(auth_user=request.user)
        formulario=Venta(anotaciones_venta=rec_anotaciones_venta,cliente_idcliente=Cliente.objects.get(idcliente=rec_cliente_idcliente),tipo_pago_idtipo_pago=TipoPago.objects.get(idtipo_pago=rec_tipo_pago_idtipo_pago),contado_venta=rec_contado_venta,vendedor_venta=Empleado.objects.get(idempleado=rec_vendedor_venta),caja_idcaja=Caja.objects.get(idcaja=rec_caja_idcaja),es_cotizacion=rec_es_cotizacion,total_venta=rec_total_venta)
        formulario.save()
        response_data = {} #declarando un diccionario vacio
        response_data['idventa']=formulario.pk
        response_data['anotaciones']=formulario.anotaciones_venta
        response_data['cliente']=fomrulario.cliente_idcliente
        response_data['tipopago']=formulario.tipo_pago_idtipo_pago
        response_data['contado']=formulario.contado_venta
        response_data['vendedor']=formulario.vendedor_venta
        response_data['caja']=formulario.caja_idcaja
        response_data['cotizacion']=formulario.es_cotizacion
        response_data['total']=formulario.total_venta
        #response_data['total']=serializers.serialize('json', list(rec_total_venta))
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def consulta_sql_personalizada(bodega,codestilo,marca,tipo,estilo,talla,color,genero):
    from django.db import connection, transaction #importando librerias para manejar directamente la BD
                                                  #con esto se salta por completo la capa de los modelos de DJANGO
    cursor = connection.cursor() #Todo se trabaja con cursores, aqui se abre la conexion

    # Data modifying operation - commit required
    #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    #transaction.commit_unless_managed()

    # Data retrieval operation - no commit required
    cursor.execute("""SELECT IP.idInventario_producto,P.codigo_producto,P.codigoestilo_producto,P.nombre_producto,Pr.valor_precio
                      FROM Producto as P
                      INNER JOIN Inventario_producto as IP on P.codigo_producto=IP.Producto_codigo_producto
                      INNER JOIN Precio as Pr on Pr.Producto_codigo_producto = P.codigo_producto
                      WHERE IP.bodega_idbodega=%s
                      AND (P.codigoestilo_producto=%s OR P.marca_idmarca = %s OR P.tipo_producto_idtipo_producto=%s OR P.estilo_idestilo=%s OR P.color_idcolor=%s OR P.genero_idgener=%s OR P.talla_idtalla=%s)""",[bodega,codestilo,marca,tipo,estilo,color,genero,talla])
    row = dictfetchall(cursor)

    return row

#la siguiente funcion/metodo, sirve para devolver los datos en forma de diccionario
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

#la siguiente funcion devuelve los datos en forma de tupla
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

#sobrecargando la funcion default de JSON
def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError
