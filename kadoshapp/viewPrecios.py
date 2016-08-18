from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pytz
import datetime #para que se pueda dar formato a la fecha
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from collections import namedtuple #Sirve en la funcion de tuplas
from decimal import Decimal #para hacer la conversion decimal a JSON
import logging #para enviar datos al archivo Debug
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql

from .models import *
from .formPrecios import *
def not_in_Supervisor_group(user):
    if user:
        return user.groups.filter(name='Supervisor').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def Precios(request):
    if request.method=='POST':
        #form_precio=Form_Precios_Precio(request.POST)
        #if form_precio.is_valid():
            #ultimo_precios=form_precio.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_producto=Form_Precios_Producto()
        form_precio=Form_Precios_Precio()
        form_InventarioProducto=Form_Precios_InventarioProducto
    return render(request, 'kadoshapp/Precios.html', {'form_InventarioProducto':form_InventarioProducto,'form_precio':form_precio,  'form_producto':form_producto })

#Vista para obtener solo el producto mediante Ajax
@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def BuscarProducto(request):
    if request.method == 'POST':
        txt_codigo_barras = request.POST.get('codigobarras_producto')
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

        resp_producto=Producto.objects.filter(Q(codigobarras_producto=txt_codigo_barras)|Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto),estado_producto=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
        if not resp_producto:
            resp_producto=Producto.objects.all().values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
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
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def BuscarPrecio(request):
    if request.method == 'POST':
        cod_producto = request.POST.get('cod_producto')
        resp_precio=Precio.objects.filter(producto_codigo_producto=Producto(pk=cod_producto)).values('pk','fechainicial_precio','fechafinal_precio','estado_precio','valor_precio','producto_codigo_producto')
        precio_diccionario=ValuesQuerySetToDict(resp_precio)
        return HttpResponse(
            json.dumps(precio_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def GuardarPrecio(request):
    if request.method == 'POST':
        cod_precio = request.POST.get('cod_precio')
        fechaini = request.POST.get('fechaini')
        fechafin = request.POST.get('fechafin')
        est_precio = request.POST.get('est_precio')
        val_precio = request.POST.get('val_precio')
        prod = request.POST.get('producto')
        if est_precio=="true":
            est_precio=1
        elif est_precio=="false":
            est_precio=0
        try:
            fini=fechaini.split('/')
            fechaini_real=datetime.datetime(int(fini[2]),int(fini[1]),int(fini[0]),0,0,0,tzinfo=pytz.UTC)
            ffin=fechafin.split('/')
            fechafin_real=None
            if len(ffin)>1:
                fechafin_real=datetime.datetime(int(ffin[2]),int(ffin[1]),int(ffin[0]),23,59,59,tzinfo=pytz.UTC)
            if not cod_precio:
                precio=Precio(fechainicial_precio=fechaini_real,fechafinal_precio=fechafin_real,estado_precio=est_precio,valor_precio=val_precio,producto_codigo_producto=Producto(pk=int(prod)))
                resultado="Nuevo precio para el producto seleccionado"
            else:
                precio=Precio(pk=int(cod_precio),fechainicial_precio=fechaini_real,fechafinal_precio=fechafin_real,estado_precio=est_precio,valor_precio=val_precio,producto_codigo_producto=Producto(pk=int(prod)))
                resultado="Precio del producto actualizado"
            precio.save()
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
