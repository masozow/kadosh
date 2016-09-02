from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formInventario import *
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql

def not_in_Bodega_group(user):
    if user:
        return user.groups.filter(name='Bodega').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

#vista Inventario
@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado')
def Inventario(request):
    if request.method=='POST':
        form_ajusteinventario=Form_Inventario_AjusteInventario(request.POST)
        form_inventario=Form_Inventario_InventarioProducto(request.POST)
        form_producto=Form_Inventario_Producto(request.POST)
        form_empleado=Form_Inventario_Empleado(request.POST)
        errores=''
        if form_ajusteinventario.is_valid():
            if form_empleado.is_valid(): #se comprueba que el formulario sea válido, es decir, que cumpla con las restricciones descritas en el model
                datosempleado=form_empleado.cleaned_data #se obtienen los datos que venían dentro de los elementos del formulario
                if datosempleado['codigo_autorizacion_empleado']: #si el codigo de autorización contiene por lo menos un dato
                    codigo=datosempleado['codigo_autorizacion_empleado'] #se obtiene el código escrito por el usuario
                    cierre=form_ajusteinventario.cleaned_data #se obtienen los datos que venían dentro de los elementos del formulario
                    empleadoautorizo=cierre['empleado_idempleado'] #se obtiene el empleado elegido en el selectinput/combobox, este es un objeto Empleado no un código como tal, esto ocurre porque esa es una llave foránea
                    empleado=Empleado.objects.filter(codigo_autorizacion_empleado=codigo,pk=empleadoautorizo.pk) #se busca el empleado que tena ese código y esa llave primaria (pk)
                    if empleado: #si existe un empleado con las dos restricciones anteriores
                        try:
                            datosajuste=form_ajusteinventario.cleaned_data
                            ajuste=form_ajusteinventario.save(commit=False)
#                            ajuste.empleado_idempleado=Empleado.objects.get(auth_user=request.user)
                            InventarioProducto.objects.filter(pk=datosajuste["inventario_producto_idinventario_producto"].pk).update(existencia_actual=datosajuste["cantidad_real_ajuste"])
                            ajuste.save()
                            form_ajusteinventario=Form_Inventario_AjusteInventario()
                            form_inventario=Form_Inventario_InventarioProducto()
                            form_producto=Form_Inventario_Producto()
                            form_empleado=Form_Inventario_Empleado()
                        except Exception as e:
                            errorForm="Error:" + str(e)
                    else:
                        errores='Los datos del empleado no coinciden'
            #form_ajusteinventario=Form_Inventario_AjusteInventario()
        return render(request, 'kadoshapp/Inventario.html', {'form_inventario':form_inventario, 'form_empleado':form_empleado , 'form_ajusteinventario':form_ajusteinventario,'form_Producto':form_producto,'errores':errores})
    else:
        errores=''
        form_inventario=Form_Inventario_InventarioProducto()
        form_producto=Form_Inventario_Producto()
        form_empleado=Form_Inventario_Empleado()
        form_ajusteinventario=Form_Inventario_AjusteInventario()
        form_ajusteinventario.fields["inventario_producto_idinventario_producto"].queryset = InventarioProducto.objects.filter(estado_inventario_producto=1)
        form_ajusteinventario.fields["motivo_idmotivo"].queryset = Motivo.objects.filter(estado_motivo=1,traslado_motivo=0)
        form_inventario.fields["bodega_idbodega"].queryset = Bodega.objects.filter(estado_bodega=1)
        form_producto.fields["marca_id_marca"].queryset = Marca.objects.filter(estado_marca=1)
        form_producto.fields["tipo_producto_idtipo_producto"].queryset = TipoProducto.objects.filter(estado_tipoproducto=1)
        form_producto.fields["estilo_idestilo"].queryset = Estilo.objects.filter(estado_estilo=1)
        form_producto.fields["talla_idtalla"].queryset = Talla.objects.filter(estado_talla=1)
        form_producto.fields["color_idcolor"].queryset = Color.objects.filter(estado_color=1)
        form_producto.fields["genero_idgener"].queryset = Genero.objects.filter(estado_genero=1)
        #form_inventariorealizado=Form_Inventario_InventarioRealizado();
    return render(request, 'kadoshapp/Inventario.html', {'form_inventario':form_inventario, 'form_empleado':form_empleado , 'form_ajusteinventario':form_ajusteinventario,'form_Producto':form_producto,'errores':errores })

@login_required
@user_passes_test(not_in_Bodega_group, login_url='denegado')
def BuscarProducto(request):
    if request.method == 'POST':
        txt_codigo_barras = request.POST.get('codigo_barras')
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
        #resp_producto=None
        if txt_codigo_barras and txt_codigo_producto and id_bodega_que_vende!= 0 and id_marca_producto !=0 and id_estilo_producto !=0 and id_tipo_producto !=0 and id_talla_producto !=0 and id_color_producto != 0 and id_genero_producto !=0:
            resp_producto=Producto.objects.filter(codigobarras_producto=txt_codigo_barras,codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,estilo_idestilo=id_estilo_producto,tipo_producto_idtipo_producto=id_tipo_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto,estado_producto=1,inventarioproducto__bodega_idbodega__pk=id_bodega_que_vende).values('pk','inventarioproducto__pk','nombre_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color','inventarioproducto__existencia_actual','estilo_idestilo__nombre_estilo','tipo_producto_idtipo_producto__nombre_tipoproducto')
        else:
            resp_producto=Producto.objects.filter(Q(codigobarras_producto=txt_codigo_barras)|Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto),estado_producto=1,inventarioproducto__bodega_idbodega__pk=id_bodega_que_vende).values('pk','inventarioproducto__pk','nombre_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color','inventarioproducto__existencia_actual','estilo_idestilo__nombre_estilo','tipo_producto_idtipo_producto__nombre_tipoproducto')
            if not resp_producto:
                resp_producto=Producto.objects.filter(inventarioproducto__bodega_idbodega__pk=id_bodega_que_vende).values('pk','inventarioproducto__pk','nombre_producto','codigoestilo_producto','marca_id_marca__nombre_marca','genero_idgener__nombre_genero','talla_idtalla__nombre_talla','color_idcolor__nombre_color','inventarioproducto__existencia_actual','estilo_idestilo__nombre_estilo','tipo_producto_idtipo_producto__nombre_tipoproducto')
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
