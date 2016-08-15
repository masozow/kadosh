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

def not_in_Traslado_group(user):
    if user:
        return user.groups.filter(name='Traslado').count() != 0
    return False

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
