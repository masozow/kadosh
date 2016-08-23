from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formModificarVenta import *
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.db.models import Q,F,ExpressionWrapper,FloatField #para poder usar el operador | que funciona como OR
#from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
import pytz #para usar la zona horaria
import datetime #para que se pueda dar formato a la fecha

def not_in_Caja_group(user):
    if user:
        return user.groups.filter(name='Caja').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]
#vista Modificar Venta
@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def ModificarVenta(request):
    if request.method=='POST':
        #form_Venta=Form_ModificarVenta_Venta(request.POST)
        #if form_Venta.is_valid():
        #    ultima_anulacionventa=form_Venta.save()
        form_Venta=Form_ModificarVenta_Venta()
        form_Cliente=Form_ModificarVenta_Cliente()
        form_DetalleVenta=Form_ModificarVenta_DetalleVenta()
        form_empleado=Form_ModificarVenta_Empleado()
        form_persona=Form_ModificarVenta_Persona()
        form_producto=Form_ModificarVenta_Producto()
        form_inventario=Form_ModificarVenta_InventarioProducto()
        form_busquedas=Form_ModificarVenta_busquedas()
        form_inventario.fields["bodega_idbodega"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
        form_Venta["empleado_idempleado"].queryset = Empleado.objects.filter(estado_empleado=1) #.exclude(codigo_autorizacion_empleado__exact='',codigo_autorizacion_empleado__isnull=True)
        form_DetalleVenta.fields["venta_idventa"].queryset = Venta.objects.filter(estado_venta=1)
        return render(request, 'kadoshapp/ModificarVenta.html', {'form_persona':form_persona,  'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_DetalleVenta':form_DetalleVenta, 'form_empleado':form_empleado,'form_producto':form_producto,'form_inventario':form_inventario,'form_busquedas':form_busquedas })
    else:
        form_Venta=Form_ModificarVenta_Venta()
        form_Cliente=Form_ModificarVenta_Cliente()
        form_DetalleVenta=Form_ModificarVenta_DetalleVenta()
        form_empleado=Form_ModificarVenta_Empleado()
        form_persona=Form_ModificarVenta_Persona()
        form_producto=Form_ModificarVenta_Producto()
        form_inventario=Form_ModificarVenta_InventarioProducto()
        form_busquedas=Form_ModificarVenta_busquedas()
        form_inventario.fields["bodega_idbodega"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
        form_Venta["empleado_idempleado"].queryset = Empleado.objects.filter(estado_empleado=1) #.exclude(codigo_autorizacion_empleado__exact='',codigo_autorizacion_empleado__isnull=True)
        form_DetalleVenta.fields["venta_idventa"].queryset = Venta.objects.filter(estado_venta=1)
        form_Venta["empleado_idempleado"].queryset = Empleado.objects.filter(estado_empleado=1) #.exclude(codigo_autorizacion_empleado__exact='',codigo_autorizacion_empleado__isnull=True)
        form_DetalleVenta.fields["venta_idventa"].queryset = Venta.objects.filter(estado_venta=1)
    return render(request, 'kadoshapp/ModificarVenta.html', {'form_persona':form_persona,  'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_DetalleVenta':form_DetalleVenta, 'form_empleado':form_empleado,'form_producto':form_producto,'form_inventario':form_inventario,'form_busquedas':form_busquedas })

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def BuscarVenta(request):
    if request.method == 'POST':
        cod_venta = request.POST.get('numeroventa')
        apellidos=request.POST.get('apellidos')
        nombres=request.POST.get('nombres')
        fecha=request.POST.get('fecha')
        nit=request.POST.get('nit')

        id_bodega_que_vende = request.POST.get('bodega_idbodega') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
        if not cod_venta:
            cod_venta=0
        f=fecha.split('/') #se hace un split con la fecha
        fechafinal_real=None  #se setea la fecha a Null
        fechainicial_real=None #se setea la fecha a Null
        if len(f)>1: #si la fecha no estaba vacia, el arreglo del split contendrá más de un elemento
            fechainicial_real=datetime.datetime(int(f[2]),int(f[1]),int(f[0]),0,0,0,tzinfo=pytz.UTC) #se obtiene la fecha con la primer hora del día
            fechafinal_real=datetime.datetime(int(f[2]),int(f[1]),int(f[0]),23,59,59,tzinfo=pytz.UTC) #se obtiene la fecha con la última hora dle día
        resp_venta=Venta.objects.filter(Q(pk=int(cod_venta))|Q(cliente_idcliente__persona_idpersona__nombres_persona=nombres) | Q(cliente_idcliente__persona_idpersona__apellidos_persona=apellidos) | Q(cliente_idcliente__nit_cliente=nit )|Q(fecha_venta__range=(fechainicial_real,fechafinal_real)),estado_venta=1).values('pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona','fecha_venta','vendedor_venta__pk','empleado_idempleado__pk','total_venta').order_by('pk')
        #if not resp_venta:
        #    resp_venta=Venta.objects.filter(estado_venta=1).values('pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona','fecha_venta','vendedor_venta','empleado_idempleado','total_venta').order_by('pk')
        venta_diccionario=ValuesQuerySetToDict(resp_venta)
        return HttpResponse(
            json.dumps(venta_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def BuscarDetalleVenta(request):
    if request.method == 'POST':
        cod_venta = request.POST.get('numeroventa')
        if not cod_venta:
            cod_venta=0
        resp_detalleventa=DetalleVenta.objects.filter(venta_idventa__pk=cod_venta).values('pk','inventario_producto_idinventario_producto__pk','inventario_producto_idinventario_producto__producto_codigo_producto__pk','inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto','cantidad_venta','valor_parcial_venta','inventario_producto_idinventario_producto__producto_codigo_producto__marca_id_marca__nombre_marca','inventario_producto_idinventario_producto__producto_codigo_producto__talla_idtalla__nombre_talla','inventario_producto_idinventario_producto__producto_codigo_producto__color_idcolor__nombre_color','inventario_producto_idinventario_producto__producto_codigo_producto__genero_idgener__nombre_genero').annotate(precio=ExpressionWrapper(F('valor_parcial_venta')/F('cantidad_venta'),output_field=FloatField()))
        #if not resp_venta:
        #    resp_venta=Venta.objects.filter(estado_venta=1).values('pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona','fecha_venta','vendedor_venta','empleado_idempleado','total_venta').order_by('pk')
        detalleventa_diccionario=ValuesQuerySetToDict(resp_detalleventa)
        return HttpResponse(
            json.dumps(detalleventa_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



def ModificacionVenta(request):
    if request.method == 'POST':
        cod_venta = request.POST.get('cod_venta')
        cod_empleado = request.POST.get('cod_empleado')
        codigo = request.POST.get('codigo')
        if not cod_empleado:
            cod_empleado=0
        if not codigo:
            resultado="No introdujo ningún código"
        else:
            empleado=Empleado.objects.filter(codigo_autorizacion_empleado=codigo,pk=cod_empleado)
            if not empleado:
                resultado="El código no pertenece al empleado"
            else:
                try:
                    Venta.objects.filter(pk=cod_venta).update(estado_venta=0)
                    resultado="Venta anulada" #no alterar este texto, porque se usa en una comprobación en la función "done" de Ajax
                except Exception as e:
                    resultado="Error: "+str(e)
        #form_precio=Form_Precios_Precio(request.POST)
        #if form_precio.is_valid():
        #    try:
        #        form_precio.is_valid()
        #        resultado="formulario guardado"
        #    except Exception as e:
        #        resultado="Error: "+str(e)
        return HttpResponse(
            json.dumps(resultado,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
def BuscarProductoNuevo(request):
    if request.method == 'POST':
        txt_codigo_barras = request.POST.get('codigobarras_producto')
        txt_codigo_producto = request.POST.get('codigo_estilo_producto')

        id_bodega_que_vende = request.POST.get('bodega') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
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
        #response_data={}
        #response_data['datos']=str(txt_codigo_barras)+'-'+str(txt_codigo_producto)+'-'+str(id_bodega_que_vende)+'-'+str(id_marca_producto)+'-'+str(id_tipo_producto)+'-'+str(id_estilo_producto)+'-'+str(id_color_producto)+'-'+str(id_genero_producto)+'-'+str(id_talla_producto)
        resp_producto=Producto.objects.filter(Q(codigobarras_producto=txt_codigo_barras)|Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto),estado_producto=1,inventarioproducto__bodega_idbodega__pk=int(id_bodega_que_vende)).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color','inventarioproducto__pk')
        producto_diccionario=ValuesQuerySetToDict(resp_producto)
        consulta=resp_producto.query
        return HttpResponse(
            json.dumps(str(consulta),cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def BuscarProductoDetalle(request):
    if request.method == 'POST':
        detalleventa=request.POST.get('detalleventa')
        if not detalleventa:
            detalleventa=0
        resp_producto=DetalleVenta.objects.filter(pk=detalleventa).values('cantidad_venta',
                                                                          'inventario_producto_idinventario_producto__pk',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__pk',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__codigobarras_producto',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__codigoestilo_producto',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__marca_id_marca__pk',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__genero_idgener__pk',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__talla_idtalla__pk',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__color_idcolor__pk',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__tipo_producto_idtipo_producto__pk',
                                                                          'inventario_producto_idinventario_producto__producto_codigo_producto__estilo_idestilo__pk',
                                                                          'inventario_producto_idinventario_producto__bodega_idbodega__pk')
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
