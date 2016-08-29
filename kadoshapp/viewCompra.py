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
from django.db.models import F

#se define a que grupo no permitir acceso
def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado') #linea para no permitir acceso al grupo
#Vista de form de compra
def Compra(request):
    if request.method=='POST':
        form_Compra=Form_Compra_Compra(request.POST)
        form_Proveedor=Form_Compra_Proveedor(request.POST)
        form_Detallecompra=Form_Compra_DetalleCompra(request.POST)
        form_InventarioProducto=Form_Compra_InventarioProducto(request.POST)
        form_Producto=Form_Compra_Producto(request.POST)
        form_fotografia=Form_Compra_Fotografia(request.POST)
        form_tabla=FormTabla(request.POST)
        form_casamatriz=FormBuscar(request.POST)
        form_precio=Form_Compra_Precio(request.POST)

        empleado=Empleado.objects.get(auth_user=request.user)
        if form_Compra.is_valid():
            #datoscompra=form_compra.cleaned_data
            ultimacompra=form_Compra.save(commit=False)
            ultimacompra.empleado_idempleado=empleado
            ultimacompra.save()
            if form_tabla.is_valid():
                datos_tabla = form_tabla.cleaned_data #se obtienen los datos que vienen en el formulario
                tablaJson = json.loads(datos_tabla['jsonfield']) #el loads es necesario, si no los datos aparecen como un arreglo, incluidos los corchetes y las comas, y no como un objeto de json que se pueda iterar
                #Iterando dentro de los arreglos de json:
                for fila in tablaJson:
                    datos=[] #creando una lista
                    for elemento in fila: #revisando los datos de cada elemneto (celda) en la fila
                        datos.append(elemento) #agregando datos a la lista
                    invent=InventarioProducto.objects.get(bodega_idbodega=datos[0],producto_codigo_producto=datos[1])
                    detalle=DetalleCompra(compra_idcompra=ultimacompra,cantidad_compra=datos[2],inventario_producto_idinventario_producto=invent,valor_parcial_compra=datos[3])
                    detalle.save()

                form_Compra=Form_Compra_Compra()
                form_Proveedor=Form_Compra_Proveedor()
                form_Detallecompra=Form_Compra_DetalleCompra()
                form_InventarioProducto=Form_Compra_InventarioProducto()
                form_Producto=Form_Compra_Producto()
                form_fotografia=Form_Compra_Fotografia()
                form_tabla=FormTabla()
                form_casamatriz=FormBuscar()
                form_precio=Form_Compra_Precio()

        form_InventarioProducto.fields["producto_codigo_producto"].queryset=Producto.objects.filter(estado_producto=1)
        form_Compra.fields["casa_matriz"].queryset=Proveedor.objects.filter(casa_matrizproveedor=1)
        form_Compra.fields["empleado_reviso"].queryset=Empleado.objects.filter(estado_empleado=1)
        form_Compra.fields["empleado_recibio"].queryset=Empleado.objects.filter(estado_empleado=1)
        form_Compra.fields["tipo_pago_idtipo_pago"].queryset=TipoPago.objects.filter(estado_tipopago=1)
        form_InventarioProducto.fields["bodega_idbodega"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_Producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_Producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_Producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_Producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_Producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_Producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
        form_TipoProducto=Form_Compra_TipoProducto()
        return render(request, 'kadoshapp/Compra.html', {'form_Proveedor':form_Proveedor, 'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto, 'form_Compra':form_Compra,'form_tabla':form_tabla,'form_casamatriz':form_casamatriz,'form_precio':form_precio })
    else:
        form_Compra=Form_Compra_Compra()
        form_Proveedor=Form_Compra_Proveedor
        form_Detallecompra=Form_Compra_DetalleCompra()
        form_InventarioProducto=Form_Compra_InventarioProducto()
        form_Producto=Form_Compra_Producto()
        form_fotografia=Form_Compra_Fotografia()
        form_tabla=FormTabla()
        form_casamatriz=FormBuscar()
        form_precio=Form_Compra_Precio()

        form_InventarioProducto.fields["producto_codigo_producto"].queryset=Producto.objects.filter(estado_producto=1)
        form_InventarioProducto.fields["bodega_idbodega"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_Compra.fields["casa_matriz"].queryset=Proveedor.objects.filter(casa_matrizproveedor=1)
        form_Compra.fields["empleado_reviso"].queryset=Empleado.objects.filter(estado_empleado=1)
        form_Compra.fields["empleado_recibio"].queryset=Empleado.objects.filter(estado_empleado=1)
        form_Compra.fields["tipo_pago_idtipo_pago"].queryset=TipoPago.objects.filter(estado_tipopago=1)
        form_Producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_Producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_Producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_Producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_Producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_Producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
        #form_anaquel=Form_Compra_Anaquel()
        form_TipoProducto=Form_Compra_TipoProducto()
    return render(request, 'kadoshapp/Compra.html', {'form_Proveedor':form_Proveedor, 'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto, 'form_Compra':form_Compra,'form_tabla':form_tabla,'form_casamatriz':form_casamatriz,'form_precio': form_precio})

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado') #linea para no permitir acceso al grupo
def SubirImagen(request): #también sirve para subir todo lo relacionado al producto e inventario
    if request.method == 'POST':
        fotografia = Form_Compra_Fotografia(data=request.POST, files=request.FILES)
        producto=Form_Compra_Producto(request.POST)
        inventario=Form_Compra_InventarioProducto(request.POST)
        detalle=Form_Compra_DetalleCompra(request.POST)
        precio=Form_Compra_Precio(request.POST)
        response_data={}
        foto=None
        if fotografia.is_valid():
            foto=fotografia.save(commit=False)
            foto.principal_fotografia=True
            foto.save()
            response_data['idfoto']=foto.pk
        else:
            response_data['error']='imagen no válida'
        if detalle.is_valid():
            datosdetalle=detalle.cleaned_data
            cantidad=datosdetalle['cantidad_compra']
            valor=datosdetalle['valor_parcial_compra']
            if inventario.is_valid():
                datosinventario=inventario.cleaned_data
                bodega=datosinventario['bodega_idbodega']
                prod=datosinventario['producto_codigo_producto']
                if producto.is_valid():
                    datosproducto=producto.cleaned_data
                    codigobarras=datosproducto['codigobarras_producto']
                    codigoestilo=datosproducto['codigoestilo_producto']
                    nombreproducto=datosproducto['nombre_producto']
                    tipoproducto=datosproducto['tipo_producto_idtipo_producto']
                    estiloproducto=datosproducto['estilo_idestilo']
                    descripcion=datosproducto['descripcion_producto']
                    marcaproducto=datosproducto['marca_id_marca']
                    colorproducto=datosproducto['color_idcolor']
                    tallaproducto=datosproducto['talla_idtalla']
                    generoproducto=datosproducto['genero_idgener']
                    if precio.is_valid():
                        datosprecio=precio.cleaned_data
                        valor=datosprecio['valor_precio']
                        if not prod: #comprobando que no se haya enviado un código de producto a través del select input (combobox)
                            prod=Producto.objects.filter(codigobarras_producto=codigobarras,codigoestilo_producto=codigoestilo,talla_idtalla=tallaproducto,genero_idgener=generoproducto,color_idcolor=colorproducto,tipo_producto_idtipo_producto=tipoproducto,estilo_idestilo=estiloproducto,marca_id_marca=marcaproducto) #comprobando la existencia de ese producto, mediante el código de barras y sus caractersíticas
                            response_data['producto']=ValuesQuerySetToDict(prod.values('pk')) #eligiendo solamente la llave primaria y guardándola en el diccionario que se regresa a través de JSON
                            if prod: #si existe el producto, se procederá a guardar el inventario y el precio
                                resultadoprecio=Precio(producto_codigo_producto=Producto(pk=response_data['producto'][0]['pk']),valor_precio=valor) #creando una nueva instancia de producto, para ese prodcuto cone sa PK y con ese Valor
                                resultadoinventario=InventarioProducto.objects.filter(bodega_idbodega=bodega,producto_codigo_producto=prod).update(existencia_actual=F('existencia_actual') + cantidad) #se actualiza el inventario de ese producto en esa bodega
                                if not resultadoinventario: #si no existiera el inventario para actualizar, entonces se crea otro nuevo
                                    resultadoinventario=InventarioProducto(producto_codigo_producto=Producto(pk=response_data['producto'][0]['pk']),bodega_idbodega=bodega,existencia_actual=cantidad) #creando el nuevo inventario
                                    resultadoinventario.save()
                            else: #si no existe el producto, se crea uno nuevo
                                prod=Producto(codigobarras_producto=codigobarras,codigoestilo_producto=codigoestilo,nombre_producto=nombreproducto,descripcion_producto=descripcion,talla_idtalla=tallaproducto,genero_idgener=generoproducto,color_idcolor=colorproducto,tipo_producto_idtipo_producto=tipoproducto,estilo_idestilo=estiloproducto,marca_id_marca=marcaproducto) #Creando el nuevo producto
                                prod.save()
                                response_data['producto']=prod.pk
                                #resultadoinventario=InventarioProducto.objects.filter(bodega_idbodega=bodega,producto_codigo_producto=prod).update(existencia_actual=F('existencia_actual') + cantidad) #se actualiza el inventario de ese producto en esa bodega
                                #if not resultadoinventario: #si no existiera el inventario para actualizar, entonces se crea otro nuevo
                                resultadoinventario=InventarioProducto(producto_codigo_producto=prod,bodega_idbodega=bodega,existencia_actual=cantidad)
                                resultadoprecio=Precio(producto_codigo_producto=prod,valor_precio=valor)
                                resultadoinventario.save()
                            resultadoprecio.save()
                        else: #si el producto elegido en el combobox no estuviera vacio, es decir, sí se envió un producto a través del select
                            resultadoinventario=InventarioProducto.objects.filter(bodega_idbodega=bodega,producto_codigo_producto=prod).update(existencia_actual=F('existencia_actual') + cantidad)
                            if not resultadoinventario: #si no existiera el inventario para actualizar, entonces se crea otro nuevo
                                resultadoinventario=InventarioProducto(producto_codigo_producto=prod,bodega_idbodega=bodega,existencia_actual=cantidad)
                                resultadoinventario.save()
                            produ=Producto.objects.filter(pk=prod.pk)
                            response_data['producto']=ValuesQuerySetToDict(produ)
                            resultadoprecio=Precio(producto_codigo_producto=prod,valor_precio=valor)
                            resultadoprecio.save()
                        #response_data['inventario']=ValuesQuerySetToDict(resultadoinventario.values('pk'))
                        response_data['bodega']=bodega.pk
                        if foto: #si hay alguna foto, se asigna al producto
                            try:
                                productoimagen=ProductoHasFotografia(fotografia_idfotografia=foto,producto_codigo_producto=prod)
                                productoimagen.save()
                            except Exception as e:
                                response_data['errorfotoproducto']=str(e)
                    else:
                        response_data['errorprecio']=precio.errors
                else:
                    response_data['errorproducto']=producto.errors
            else:
                response_data['errorinventario']=inventario.errors
        else:
            response_data['errordetalle']=detalle.errors

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

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado') #linea para no permitir acceso al grupo
def BuscarProducto(request):
    if request.method == 'POST':
        txt_codigo_barras = request.POST.get('codigobarras_producto')
        resp_producto=Producto.objects.filter(codigobarras_producto=txt_codigo_barras).values('pk','nombre_producto','descripcion_producto','codigobarras_producto','codigoestilo_producto','estilo_idestilo__pk','tipo_producto_idtipo_producto__pk','marca_id_marca__pk','genero_idgener__pk','talla_idtalla__pk','color_idcolor__pk','descripcion_producto')
        #resp_producto=Producto.objects.filter(marca_id_marca=id_marca_producto,estilo_idestilo=id_estilo_producto,tipo_producto_idtipo_producto=id_tipo_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
        producto_diccionario=ValuesQuerySetToDict(resp_producto)
        return HttpResponse(
            json.dumps(producto_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado') #linea para no permitir acceso al grupo
def BuscarProductoEstilo(request):
    if request.method == 'POST':
        txt_codigo_estilo = request.POST.get('codigoestilo_producto')
        resp_producto=Producto.objects.filter(codigoestilo_producto=txt_codigo_estilo).values('pk','nombre_producto','descripcion_producto','codigobarras_producto','codigoestilo_producto','estilo_idestilo__pk','tipo_producto_idtipo_producto__pk','marca_id_marca__pk','genero_idgener__pk','talla_idtalla__pk','color_idcolor__pk','descripcion_producto')
        #resp_producto=Producto.objects.filter(marca_id_marca=id_marca_producto,estilo_idestilo=id_estilo_producto,tipo_producto_idtipo_producto=id_tipo_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
        producto_diccionario=ValuesQuerySetToDict(resp_producto)
        return HttpResponse(
            json.dumps(producto_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado') #linea para no permitir acceso al grupo
def BuscarProductoCaracteristicas(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigo_estilo_producto')

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
        resp_producto=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto).values('pk','nombre_producto','descripcion_producto','codigoestilo_producto','estilo_idestilo__nombre_estilo','tipo_producto_idtipo_producto__nombre_tipoproducto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
        if not resp_producto:
            if id_estilo_producto=='1' and id_tipo_producto=='1' and id_talla_producto=='1' and id_color_producto=='1' and id_genero_producto=='1':
                resp_producto=Producto.objects.filter(marca_id_marca=id_marca_producto).values('pk','nombre_producto','descripcion_producto','codigoestilo_producto','estilo_idestilo__nombre_estilo','tipo_producto_idtipo_producto__nombre_tipoproducto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
            else:
                resp_producto=Producto.objects.filter(Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto), marca_id_marca=id_marca_producto).values('pk','nombre_producto','descripcion_producto','codigoestilo_producto','estilo_idestilo__nombre_estilo','tipo_producto_idtipo_producto__nombre_tipoproducto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')

        #if not resp_producto:resp_producto=Producto.objects.filter(|Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto)).values('pk','nombre_producto','descripcion_producto','codigoestilo_producto','estilo_idestilo__nombre_estilo','tipo_producto_idtipo_producto__nombre_tipoproducto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
        #    resp_producto=Producto.objects.all().values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
        producto_diccionario=ValuesQuerySetToDict(resp_producto)
        return HttpResponse(
            json.dumps(producto_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado') #linea para no permitir acceso al grupo
def GuardarObtenerProveedor(request):
    if request.method == 'POST':
        nit = request.POST.get('nit')
        proveedor = request.POST.get('proveedor')
        casa=request.POST.get('casa')
        try:
            proveedor=Proveedor(nombre_proveedor=proveedor,nit_proveedor=nit,casa_matrizproveedor=int(casa))
            proveedor.save()
            resp_proveedor=Proveedor.objects.filter(estado_proveedor=1,casa_matrizproveedor=int(casa)).values('pk','nombre_proveedor')
            dic_proveedor=ValuesQuerySetToDict(resp_proveedor)
        except Exception as e:
            dic_proveedor='Ha ocurrido un error. Intente de nuevo' #no cambiar este mensaje, porque de el depende una alerta en la plantilla

        return HttpResponse(
            json.dumps(dic_proveedor,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
