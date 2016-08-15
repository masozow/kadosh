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

def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

#El siguiente método convierte el resultado de "values" en un diccionario
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

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
        resultado=Producto.objects.filter(codigobarras_producto=txt_codigo_producto).values('pk',
                                                                                            'nombre_producto',
                                                                                            'inventarioproducto__bodega_idbodega__nombre_bodega',
                                                                                            'codigobarras_producto',
                                                                                            'inventarioproducto__existencia_actual',
                                                                                            'codigoestilo_producto',
                                                                                            'precio__valor_precio',
                                                                                            'marca_id_marca__nombre_marca')
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


        #La Q en el siguiente queryset es importantisima, sin ella no funciona los OR, representados por el operador |
        resultado=Producto.objects.filter(Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto)).values('pk',
                                                                                                                                                                                                                                                                                                                                                      'nombre_producto',
                                                                                                                                                                                                                                                                                                                                                      'inventarioproducto__bodega_idbodega__nombre_bodega',
                                                                                                                                                                                                                                                                                                                                                      'codigobarras_producto',
                                                                                                                                                                                                                                                                                                                                                      'inventarioproducto__existencia_actual',
                                                                                                                                                                                                                                                                                                                                                      'codigoestilo_producto',
                                                                                                                                                                                                                                                                                                                                                      'precio__valor_precio',
                                                                                                                                                                                                                                                                                                                                                      'marca_id_marca__nombre_marca')

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
