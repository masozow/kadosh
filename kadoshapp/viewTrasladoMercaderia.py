from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formTrasladoMercaderia import *
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.db.models import Q #para poder usar el operador | que funciona como OR
from collections import namedtuple #Sirve en la funcion de tuplas
from decimal import Decimal #para hacer la conversion decimal a JSON
import logging #para enviar datos al archivo Debug

def not_in_Traslado_group(user):
    if user:
        return user.groups.filter(name='Traslado').count() != 0
    return False
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]
#CVista de Traslado de mercaderia
@login_required
@user_passes_test(not_in_Traslado_group, login_url='denegado')
def TrasladoMercaderia(request):
    if request.method=='POST':
        empleado=Empleado.objects.get(auth_user=request.user) #Obteniendo el empleado logueado
        form_Traslado=Form_TrasladoMerca_TrasaladoMercaderia(request.POST) #obteniendo el form que vino con el request
        form_productos=FormTabla(request.POST) #obteniendo el segundo form que vino con el request
        if form_Traslado.is_valid(): #si el formulario de traslado es vállido
            datos_traslado=form_Traslado.cleaned_data #con cleaned_data ya se puede acceder a los datos que contiene el form
            ultimo_traslado=form_Traslado.save(commit=False) #Se obtienen los datos pero no se guardan aún
            ultimo_traslado.empleado_idempleado=empleado #asignando el empleado logueado
            ultimo_traslado=form_Traslado.save() #ahora sí se guardan
            if form_productos.is_valid(): #si el segundo formulario, el de traslados es válido
                datos_tabla = form_productos.cleaned_data #se obtienen los datos que vienen en el formulario
                tablaJson = json.loads(datos_tabla['jsonfield']) #el loads es necesario, si no los datos aparecen como un arreglo, incluidos los corchetes y las comas, y no como un objeto de json que se pueda iterar
                #Iterando dentro de los arreglos de json:
                for fila in tablaJson:
                    datos=[] #creando una lista
                    for elemento in fila: #revisando los datos de cada elemneto (celda) en la fila
                        datos.append(elemento) #agregando datos a la lista
                    InventarioProducto.objects.filter(bodega_idbodega=datos_traslado['bodega_egreso'],producto_codigo_producto=Producto(pk=datos[0])).update(existencia_actual=F('existencia_actual') - datos[1]) #Haciendo un update a las existencias del inventario que que contenga esa bodega y ese prducto
                    resultado=InventarioProducto.objects.filter(bodega_idbodega=datos_traslado['bodega_ingreso'],producto_codigo_producto=Producto(pk=datos[0])).update(existencia_actual=F('existencia_actual') + datos[1]) #Haciendo un update a las existencias del inventario que contenga esa bodega y ese prducto, y además se guarda el resultado en una variable
                    if not resultado: #Si ese inventario no existiera, se realiza lo siguiente
                        NuevoInventario=InventarioProducto(bodega_idbodega=datos_traslado['bodega_ingreso'],producto_codigo_producto=Producto(pk=datos[0]),existencia_actual=datos[1]) #Se crea un nuevo inventario para ese producto, en esa bodega
                        NuevoInventario.save() #Guardando el nuevo inventario

        #Los siguientes forms solo se envian para cuando la página se recarga luego de enviar los datos,
        #así se pueden renderizar los controles del inventario, si no se envían, la plantilla aparece vacía
        form_Traslado=Form_TrasladoMerca_TrasaladoMercaderia()
        form_Producto=Form_TrasladoMerca_Producto()
        form_InventarioProducto=Form_TrasladoMerca_InventarioProducto()
        form_cantidad=Form_TrasladoMerca_Cantidad()
        form_Tabla=FormTabla()
        #A continuación se filtran los datos de los combobox, para que se muestren solo los que cumplan con las condiciones
        #descritas en el filtro
        form_Traslado.fields["bodega_egreso"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_Traslado.fields["bodega_ingreso"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_Traslado.fields["motivo_idmotivo"].queryset = Motivo.objects.filter(estado_motivo=1,traslado_motivo=1)
        form_Producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_Producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_Producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_Producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_Producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_Producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
        return render(request, 'kadoshapp/TrasladoMerca.html', {'form_Producto':form_Producto ,'form_InventarioProducto':form_InventarioProducto, 'form_Tabla':form_Tabla,'form_Traslado':form_Traslado, 'form_cantidad':form_cantidad })
    else:
        form_Traslado=Form_TrasladoMerca_TrasaladoMercaderia()
        form_Producto=Form_TrasladoMerca_Producto()
        form_InventarioProducto=Form_TrasladoMerca_InventarioProducto()
        form_cantidad=Form_TrasladoMerca_Cantidad()
        form_Tabla=FormTabla()
        #A continuación se filtran los datos de los combobox, para que se muestren solo los que cumplan con las condiciones
        #descritas en el filtro
        form_Traslado.fields["bodega_egreso"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_Traslado.fields["bodega_ingreso"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_Traslado.fields["motivo_idmotivo"].queryset = Motivo.objects.filter(estado_motivo=1,traslado_motivo=1)
        form_Producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_Producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_Producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_Producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_Producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_Producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
    return render(request, 'kadoshapp/TrasladoMerca.html', {'form_Producto':form_Producto ,'form_InventarioProducto':form_InventarioProducto, 'form_Tabla':form_Tabla,'form_Traslado':form_Traslado, 'form_cantidad':form_cantidad })

@login_required
@user_passes_test(not_in_Traslado_group, login_url='denegado')
def BuscarProducto(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigobarras_producto')
        id_bodega_que_vende = request.POST.get('bodega_idbodega') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
        if not id_bodega_que_vende:
            id_bodega_que_vende=0
        response_data = {} #declarando un diccionario vacio
        producto=Producto.objects.filter(codigobarras_producto=txt_codigo_producto,estado_producto=1,inventarioproducto__bodega_idbodega=id_bodega_que_vende,precio__estado_precio=1).values('pk','nombre_producto','marca_id_marca__nombre_marca','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','inventarioproducto__pk','precio__valor_precio','precio__pk').order_by('-precio__pk')[:1]
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
@user_passes_test(not_in_Traslado_group, login_url='denegado')
def BuscarProductoCaracteristicas(request):
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



def consulta_sql_personalizada(bodega,codestilo,marca,tipo,estilo,talla,color,genero):
    from django.db import connection, transaction #importando librerias para manejar directamente la BD
                                                  #con esto se salta por completo la capa de los modelos de DJANGO
    cursor = connection.cursor() #Todo se trabaja con cursores, aqui se abre la conexion

    # Data modifying operation - commit required
    #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    #transaction.commit_unless_managed()

    # Data retrieval operation - no commit required
    cursor.execute("""SELECT IP.idInventario_producto,P.codigo_producto,P.codigoestilo_producto,P.nombre_producto,Pr.valor_precio,M.nombre_marca,T.nombre_talla,G.nombre_genero,C.nombre_color
                      FROM Producto as P
                      INNER JOIN Inventario_producto as IP on P.codigo_producto=IP.Producto_codigo_producto
                      INNER JOIN Precio as Pr on Pr.Producto_codigo_producto = P.codigo_producto
                      INNER JOIN Marca as M on M.id_marca = P.marca_idmarca
                      INNER JOIN Talla as T on T.idtalla = P.talla_idtalla
                      INNER JOIN Genero as G on G.idgener=P.genero_idgener
                      INNER JOIN Color as C on C.idcolor=P.color_idcolor
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

#sobrecargando la funcion default de JSON, para poder enviar datos decimales
def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError
