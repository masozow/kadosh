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
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.db.models import Q #para poder usar el operador | que funciona como OR

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def not_in_Traslado_group(user):
    if user:
        return user.groups.filter(name='Traslado').count() != 0
    return False

@login_required
@user_passes_test(not_in_Traslado_group, login_url='denegado')
def Listado(request):
    if request.method=='POST':
        form_producto=Form_Listado_Producto(request.POST)
        form_busqueda=Form_busquedas(request.POST)
    else:
        form_producto=Form_Listado_Producto()
        form_busqueda=Form_busquedas()
    return render(request, 'kadoshapp/ListadoProductos.html', {'form_producto':form_producto,'form_busqueda':form_busqueda })

@login_required
def BuscarProductoExtra(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigobarras_producto')
        #runeval(txt_codigo_producto) #se supone que evalua la variable y la envia al debugger
        #pdb.set_trace()  #estos son los breakpoints de django

        response_data = {} #declarando un diccionario vacio
        resultado=Producto.objects.filter(codigobarras_producto=txt_codigo_producto,estado_producto=1,precio__estado_precio=1).values('pk',
                                                                                            'nombre_producto',
                                                                                            'inventarioproducto__bodega_idbodega__nombre_bodega',
                                                                                            'codigobarras_producto',
                                                                                            'inventarioproducto__existencia_actual',
                                                                                            'codigoestilo_producto',
                                                                                            'precio__valor_precio',
                                                                                            'marca_id_marca__nombre_marca',
                                                                                            'tipo_producto_idtipo_producto__nombre_tipoproducto',
                                                                                            'estilo_idestilo__nombre_estilo',
                                                                                            'genero_idgener__nombre_genero',
                                                                                            'talla_idtalla__nombre_talla',
                                                                                            'color_idcolor__nombre_color')
                                                                            #'inventarioproducto__detallecompra__valor_parcial_compra'
                                                                            #).order_by('-inventarioproducto__detallecompra__pk')
        resultado_diccionario=ValuesQuerySetToDict(resultado)
        return HttpResponse(
            json.dumps(resultado_diccionario,cls=DjangoJSONEncoder),
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

        resp_producto=Producto.objects.filter(estado_producto=1,precio__estado_precio=1).values('pk','nombre_producto','inventarioproducto__bodega_idbodega__nombre_bodega','codigobarras_producto','inventarioproducto__existencia_actual','codigoestilo_producto','precio__valor_precio','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','estilo_idestilo__nombre_estilo','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
        
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


        resultado_diccionario=ValuesQuerySetToDict(resp_producto)
        return HttpResponse(
            json.dumps(resultado_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
def BuscarProductoAutocompletarExtra(request):
    if request.method == 'POST':
        txt_producto = str(request.POST.get('producto_buscado'))
        producto=Producto.objects.filter(Q(nombre_producto__icontains=txt_producto)|Q(marca_id_marca__nombre_marca__icontains=txt_producto)|Q(estilo_idestilo__nombre_estilo__icontains=txt_producto)|Q(tipo_producto_idtipo_producto__nombre_tipoproducto__icontains=txt_producto)|Q(color_idcolor__nombre_color__icontains=txt_producto)|Q(talla_idtalla__nombre_talla__icontains=txt_producto)|Q(genero_idgener__nombre_genero__icontains=txt_producto),estado_producto=1,precio__estado_precio=1).values('pk','nombre_producto','inventarioproducto__bodega_idbodega__nombre_bodega','codigobarras_producto','inventarioproducto__existencia_actual','codigoestilo_producto','precio__valor_precio','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','estilo_idestilo__nombre_estilo','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
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
