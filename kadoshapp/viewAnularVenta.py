from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formAnularVenta import *
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
import pytz #para usar la zona horaria
import datetime #para que se pueda dar formato a la fecha
from django.utils import timezone

def not_in_Caja_group(user):
    if user:
        return user.groups.filter(name='Caja').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]
#vista Anular Venta
@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def AnularVenta(request):
    if request.method=='POST':
        form_Venta=Form_AnulaVenta_Venta(request.POST)
        form_Cliente=Form_AnulaVenta_Cliente(request.POST)
        form_DetalleVenta=Form_AnulaVenta_DetalleVenta(request.POST)
        form_empleado=Form_AnulaVenta_Empleado(request.POST)
        form_persona=Form_AnulaVenta_Persona(request.POST)
        form_Venta["empleado_idempleado"].queryset = Empleado.objects.filter(estado_empleado=1) #.exclude(codigo_autorizacion_empleado__exact='',codigo_autorizacion_empleado__isnull=True)
        form_DetalleVenta.fields["venta_idventa"].queryset = Venta.objects.filter(estado_venta=1)
        return render(request, 'kadoshapp/AnularVenta.html', {'form_persona':form_persona,  'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_DetalleVenta':form_DetalleVenta, 'form_empleado':form_empleado })
    else:
        form_Venta=Form_AnulaVenta_Venta()
        form_Cliente=Form_AnulaVenta_Cliente()
        form_DetalleVenta=Form_AnulaVenta_DetalleVenta()
        form_empleado=Form_AnulaVenta_Empleado()
        form_persona=Form_AnulaVenta_Persona()
        form_Venta["empleado_idempleado"].queryset = Empleado.objects.filter(estado_empleado=1) #.exclude(codigo_autorizacion_empleado__exact='',codigo_autorizacion_empleado__isnull=True)
        form_DetalleVenta.fields["venta_idventa"].queryset = Venta.objects.filter(estado_venta=1)
        return render(request, 'kadoshapp/AnularVenta.html', {'form_persona':form_persona,  'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_DetalleVenta':form_DetalleVenta, 'form_empleado':form_empleado })

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
            f1=datetime.date(int(f[2]),int(f[1]),int(f[0]))
            #fechainicial_real=datetime.datetime.combine(f1,timezone.datetime.min())
            #fechafinal_real=datetime.datetime.combine(f1,timezone.datetime.max())
            fechainicial_real=datetime.datetime(int(f[2]),int(f[1]),int(f[0]),0,0,0,tzinfo=pytz.UTC) #se obtiene la fecha con la primer hora del día
            fechafinal_real=datetime.datetime(int(f[2]),int(f[1]),int(f[0]),23,59,59,tzinfo=pytz.UTC) #se obtiene la fecha con la última hora dle día
            fechainicial_real=fechainicial_real+datetime.timedelta(hours=6)
            fechafinal_real=fechafinal_real+datetime.timedelta(hours=6)
        resp_venta=Venta.objects.filter(Q(pk=int(cod_venta))|Q(cliente_idcliente__persona_idpersona__nombres_persona=nombres) | Q(cliente_idcliente__persona_idpersona__apellidos_persona=apellidos) | Q(cliente_idcliente__nit_cliente=nit )|Q(fecha_venta__range=(fechainicial_real,fechafinal_real)),estado_venta=1,es_cotizacion=0).values('pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona','fecha_venta','vendedor_venta__pk','empleado_idempleado__pk','total_venta').order_by('pk')

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
def AnulacionVenta(request):
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
                #try:
                Venta.objects.filter(pk=cod_venta).update(estado_venta=0)
                detalles=DetalleVenta.objects.filter(venta_idventa__pk=cod_venta)
                for detalle in detalles:
                    inventario=detalle.inventario_producto_idinventario_producto
                    if inventario:
                        cantidad=detalle.cantidad_venta
                        inventarioactualizado=InventarioProducto.objects.filter(pk=inventario.pk).update(existencia_actual=F('existencia_actual')+cantidad)
                resultado="Venta anulada" #no alterar este texto, porque se usa en una comprobación en la función "done" de Ajax
                #except Exception as e:
                #    resultado="Error: "+str(e)
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
