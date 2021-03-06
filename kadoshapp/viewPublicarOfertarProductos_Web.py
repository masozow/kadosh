from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formPublicarOfertarProductos_Web import *
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.db.models import Q #para poder usar el operador | que funciona como OR

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def not_in_Web_group(user):
    if user:
        return user.groups.filter(name='Web').count() != 0
    return False

@login_required
@user_passes_test(not_in_Web_group, login_url='denegado')
def publicarofertar(request):
    if request.method=='POST':
        form_producto=Form_Publicar_Producto(request.POST)
    else:
        form_producto=Form_Publicar_Producto()
    return render(request, 'kadoshapp/PublicarOfertarProductos_Web.html', {'form_producto':form_producto })

@login_required
@user_passes_test(not_in_Web_group, login_url='denegado')
def BuscarProductoExtra(request):
    if request.method == 'POST':
        txt_codigo_producto = request.POST.get('codigobarras_producto')
        #runeval(txt_codigo_producto) #se supone que evalua la variable y la envia al debugger
        #pdb.set_trace()  #estos son los breakpoints de django

        response_data = {} #declarando un diccionario vacio
        resultado=Producto.objects.filter(codigobarras_producto=txt_codigo_producto,estado_producto=1).values('pk',
                                                                                            'nombre_producto',
                                                                                            'codigobarras_producto',
                                                                                            'codigoestilo_producto',
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
@user_passes_test(not_in_Web_group, login_url='denegado')
def BuscarProductoCaracteristicasExtra(request):
    if request.method == 'POST':

        resp_producto=Producto.objects.filter(estado_producto=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','estilo_idestilo__nombre_estilo','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color')
        
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
@user_passes_test(not_in_Web_group, login_url='denegado')
def BuscarProductoEspecifico(request):
    if request.method == 'POST':
        codigo_producto = request.POST.get('codigoproducto')
        response_data = {} #declarando un diccionario vacio
        resultado=Producto.objects.filter(pk=codigo_producto).values('pk','descripcion_producto','oferta_producto','publicar_producto')
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
@user_passes_test(not_in_Web_group, login_url='denegado')
def ActualizarProducto(request):
    if request.method == 'POST':
        codigo_producto = request.POST.get('codigoproducto')
        oferta = request.POST.get('ofertar')
        publicar = request.POST.get('publicar')
        descripcion = request.POST.get('descripcionproducto')
        if oferta=='true':
            oferta=True
        else:
            oferta=False
        if publicar=='true':
            publicar=True
        else:
            publicar=False
        try:
            prod=Producto.objects.filter(pk=codigo_producto).update(oferta_producto=oferta,publicar_producto=publicar,descripcion_producto=descripcion)
            resultado='Producto actualizado' #no cambiar este texto, porque de el depende un cambio en la funcion de ajax en la plantilla
        except Exception as e:
            resultado='Error: '+str(e)        
        return HttpResponse(
            json.dumps(resultado,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
