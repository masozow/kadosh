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
import logging #para enviar datos al archivo Debug
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.contrib.auth.decorators import login_required, user_passes_test
import datetime

from .models import *
from .formPuntodeVenta import *

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

#Vista de Punto de Venta
def not_in_Caja_group(user):
    if user:
        return user.groups.filter(name='Caja').count() != 0
    return False
@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def PuntoDeVenta(request):
    if request.method=='POST':
        #form_Venta=Form_PuntoVenta_Venta(request.POST)
        #if form_Venta.is_valid():
        #    ultima_venta=form_Venta.save()
        return render(request, 'kadoshapp/PuntoDeVenta.html',{})
    else:
        form_Venta=Form_PuntoVenta_Venta()
        form_DetalleVenta=Form_PuntoVenta_DetalleVenta()
        form_InventarioProducto=Form_PuntoVenta_InventarioProducto()
        form_Producto=Form_PuntoVenta_Producto()
        form_Promocion=Form_PuntoVenta_Promocion()
        form_Precio=Form_PuntoVenta_Precio()
        form_cliente=Form_PuntoVenta_busquedas()
        form_promocionhasproducto=Form_PuntoVenta_PromocionHasProducto()
        #Se filtran los datos que pueden ser vistos en los DropDown/Comobobx
        form_Venta.fields["vendedor_venta"].queryset = Empleado.objects.filter(puesto_idpuesto__nombre_puesto__contains='Ventas',estado_empleado=1)
        #En la consulta anterior, se realizó un innerjoin, primero "puesto_idpuesto" es un campo de llave foránea hacia la tabla "Puesto",
        #luego con el doble guión bajo "__" se le indica que en la Tabla foránea, se utilizará el campo "nombre_puesto"
        #por último se le dice que busque los nombres que contengan la palabra "Ventas"
        form_Venta.fields["caja_idcaja"].queryset = Caja.objects.filter(estado_caja=1)
        form_Venta.fields["cliente_idcliente"].queryset = Cliente.objects.filter(estado_cliente=1)
        form_InventarioProducto.fields["bodega_idbodega"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_Producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_Producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_Producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_Producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_Producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_Producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
        form_DetalleVenta.fields["descuento_iddescuento"].queryset=Descuento.objects.filter(estado_descuento=1,autorizado_descuento=1)
    return render(request, 'kadoshapp/PuntoDeVenta.html', {
                    'form_Venta': form_Venta,
                    'form_DetalleVenta':form_DetalleVenta,
                    'form_Producto':form_Producto ,
                    'form_InventarioProducto':form_InventarioProducto,
                    'form_Promocion':form_Promocion,
                    'form_Precio':form_Precio,
                    'form_cliente':form_cliente,
                    'form_promocionhasproducto': form_promocionhasproducto
                    })

@login_required
#Vista para obtener solo el producto mediante Ajax
def BuscarProducto(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigobarras_producto')
        id_bodega_que_vende = request.POST.get('bodega_idbodega') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
        #runeval(txt_codigo_producto) #se supone que evalua la variable y la envia al debugger
        #pdb.set_trace()  #estos son los breakpoints de django

        response_data = {} #declarando un diccionario vacio
        producto=Producto.objects.filter(codigobarras_producto=txt_codigo_producto,estado_producto=1,inventarioproducto__bodega_idbodega=id_bodega_que_vende,precio__estado_precio=1).values('pk','nombre_producto','marca_id_marca__nombre_marca','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','inventarioproducto__pk','precio__valor_precio','precio__pk','estilo_idestilo__nombre_estilo','codigoestilo_producto').order_by('-precio__pk')
        dict_producto=ValuesQuerySetToDict(producto)

        return HttpResponse(
            json.dumps(dict_producto,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
def BuscarProductoAutocompletar(request):
    if request.method == 'POST':
        txt_producto = str(request.POST.get('producto_buscado'))
        id_bodega_que_vende = request.POST.get('bodega_idbodega')
        producto=Producto.objects.filter(Q(nombre_producto__icontains=txt_producto)|Q(marca_id_marca__nombre_marca__icontains=txt_producto)|Q(estilo_idestilo__nombre_estilo__icontains=txt_producto)|Q(tipo_producto_idtipo_producto__nombre_tipoproducto__icontains=txt_producto)|Q(color_idcolor__nombre_color__icontains=txt_producto)|Q(talla_idtalla__nombre_talla__icontains=txt_producto)|Q(genero_idgener__nombre_genero__icontains=txt_producto),estado_producto=1,inventarioproducto__bodega_idbodega=id_bodega_que_vende,precio__estado_precio=1).values('pk','nombre_producto','marca_id_marca__nombre_marca','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','inventarioproducto__pk','precio__valor_precio','precio__pk','estilo_idestilo__nombre_estilo','codigoestilo_producto').order_by('-precio__pk')
        dict_producto=ValuesQuerySetToDict(producto)

        return HttpResponse(
            json.dumps(dict_producto,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
def BuscarProductoCaracteristicas(request):
    if request.method == 'POST':
        id_bodega_que_vende = request.POST.get('bodega_idbodega') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
        if not id_bodega_que_vende:
            id_bodega_que_vende=0

        resp_producto=Producto.objects.filter(estado_producto=1,inventarioproducto__bodega_idbodega__pk=id_bodega_que_vende,precio__estado_precio=1).values('pk','nombre_producto','marca_id_marca__nombre_marca','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','inventarioproducto__pk','precio__valor_precio','precio__pk','estilo_idestilo__nombre_estilo','codigoestilo_producto').order_by('-precio__pk')
        
        txt_codigo_producto = request.POST.get('codigo_estilo_producto')
        if txt_codigo_producto:
            resp_producto=resp_producto.filter(codigoestilo_producto=txt_codigo_producto)
        
        id_marca_producto = request.POST.get('marca_producto')
        if id_marca_producto:
            resp_producto=resp_producto.filter(marca_id_marca=id_marca_producto)

        id_estilo_producto = request.POST.get('estilo_producto')
        if id_estilo_producto:
            resp_producto=resp_producto.filter(estilo_idestilo=id_estilo_producto)

        id_tipo_producto = request.POST.get('tipo_producto')
        if id_tipo_producto:
            resp_producto=resp_producto.filter(tipo_producto_idtipo_producto=id_tipo_producto)

        id_talla_producto = request.POST.get('talla_producto')
        if id_talla_producto:
            resp_producto=resp_producto.filter(talla_idtalla=id_talla_producto)

        id_color_producto = request.POST.get('color_producto')
        if id_color_producto:
            resp_producto=resp_producto.filter(color_idcolor=id_color_producto)

        id_genero_producto = request.POST.get('genero_producto')
        if id_genero_producto:
            resp_producto=resp_producto.filter(genero_idgener=id_genero_producto)

        
        resp_consulta=ValuesQuerySetToDict(resp_producto)


        return HttpResponse(
            json.dumps(resp_consulta,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
def BuscarProductoImagenPrincipal(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigo_producto')
        response_data = {} #declarando un diccionario vacio
        
        resp_foto=ProductoHasFotografia.objects.filter(producto_codigo_producto__pk=txt_codigo_producto,fotografia_idfotografia__principal_fotografia=1).values('fotografia_idfotografia__pk','fotografia_idfotografia__ruta_fotografia')
        foto=ValuesQuerySetToDict(resp_foto)
        return HttpResponse(
            json.dumps(foto,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
def GuardarVenta(request):
    if request.method == 'POST':
        #Guardando todos los datos que se recibieron a traves de Ajax:
        rec_anotaciones_venta = request.POST.get('env_anotaciones_venta')
        rec_cliente_idcliente = request.POST.get('env_cliente_idcliente')
        if not rec_cliente_idcliente: #revisando que el id de cliente no este vacio
            rec_cliente_idcliente=0
        rec_tipo_pago_idtipo_pago = request.POST.get('env_tipo_pago_idtipo_pago')
        if not rec_tipo_pago_idtipo_pago: #revisando que el id del tipo de pago no este vacio
            rec_tipo_pago_idtipo_pago=0
        rec_contado_venta = request.POST.get('env_contado_venta')
        rec_vendedor_venta = request.POST.get('env_vendedor_venta')
        if not rec_vendedor_venta:
            rec_vendedor_venta=0
        rec_caja_idcaja = request.POST.get('env_caja_idcaja')
        if not rec_caja_idcaja:
            rec_caja_idcaja=0
        rec_es_cotizacion = request.POST.get('env_es_cotizacion')
        rec_total_venta = request.POST.get('env_total_venta')
        rec_tabla=request.POST.get('tabla')
        if rec_es_cotizacion=='true':
            rec_es_cotizacion=1
        else:
            rec_es_cotizacion=0
        if rec_contado_venta=='true':
            rec_contado_venta=1
        else:
            rec_contado_venta=0

        response_data = {} #declarando un diccionario vacio
        try:
            #empleado=Empleado.objects.get(auth_user=request.user)
            ventaNueva=Venta(anotaciones_venta=rec_anotaciones_venta,cliente_idcliente=Cliente.objects.get(idcliente=rec_cliente_idcliente),tipo_pago_idtipo_pago=TipoPago.objects.get(idtipo_pago=rec_tipo_pago_idtipo_pago),contado_venta=rec_contado_venta,vendedor_venta=Empleado.objects.get(idempleado=rec_vendedor_venta),caja_idcaja=Caja.objects.get(idcaja=rec_caja_idcaja),es_cotizacion=rec_es_cotizacion,total_venta=rec_total_venta)
            ventaNueva.save()
            if rec_es_cotizacion==0 and rec_contado_venta==0:
                cuentaNueva=CuentaPorCobrar(venta_idventa=ventaNueva,saldo_inicial_cuentaporcobrar=rec_total_venta,saldo_actual_cuentaporcobrar=rec_total_venta,fecha_pagofinal_cuentaporcobrar=datetime.date.today())
                cuentaNueva.save()
            tablaJson=json.loads(rec_tabla)#el loads es necesario, si no los datos aparecen como un arreglo, incluidos los corchetes y las comas

            #Iterando dentro de los arreglos de json:
            for fila in tablaJson:
                datos=[] #creando una lista
                for elemento in fila:
                    datos.append(elemento) #agregando datos a la lista
                if datos[0]=='0': #sí es un descuento
                    detalleNuevo=DetalleVenta(venta_idventa=ventaNueva,descuento_iddescuento=Descuento(iddescuento=datos[1]),cantidad_venta=datos[2],valor_parcial_venta=datos[5])
                else: #es un producto normal
                    detalleNuevo=DetalleVenta(venta_idventa=ventaNueva,inventario_producto_idinventario_producto=InventarioProducto(pk=datos[0]),cantidad_venta=datos[2],valor_parcial_venta=datos[5])
                    if rec_es_cotizacion==0 and rec_contado_venta==1:  #solo si no es cotizacion y si es al contado, se van a actualizar las existencias
                        invent=InventarioProducto.objects.filter(pk=datos[0]).update(existencia_actual=F('existencia_actual') - datos[2]) #Haciendo un update a las existencias del inventario con esa PK
                detalleNuevo.save()
            #los siguientes datos son para revision solamente, asi se tiene una respuesta de exito en la consola
            response_data['total']=ventaNueva.total_venta
            response_data['idventa']=ventaNueva.pk
        except Exception as e:
            response_data['idventa']="Ha ocurrido un error: "+str(e)
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
    cursor.execute("""SELECT IP.idInventario_producto,P.codigo_producto,P.codigoestilo_producto,P.nombre_producto,Pr.valor_precio,M.nombre_marca,T.nombre_talla,G.nombre_genero,C.nombre_color,E.nombre_estilo
                      FROM Producto as P
                      INNER JOIN Inventario_producto as IP on P.codigo_producto=IP.Producto_codigo_producto
                      INNER JOIN Precio as Pr on Pr.Producto_codigo_producto = P.codigo_producto
                      INNER JOIN Marca as M on M.id_marca = P.marca_idmarca
                      INNER JOIN Talla as T on T.idtalla = P.talla_idtalla
                      INNER JOIN Genero as G on G.idgener=P.genero_idgener
                      INNER JOIN Color as C on C.idcolor=P.color_idcolor
                      INNER JOIN Estilo as E on E.idEstilo=P.Estilo_idEstilo
                      WHERE IP.bodega_idbodega=%s
                      AND P.estado_producto=1 AND IP.estado_inventario_producto=1 AND Pr.estado_precio=1
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

#sobrecargando la funcion default de JSON, para poder enviar datos decimales
def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError
