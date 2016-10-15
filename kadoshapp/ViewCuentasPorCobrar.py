from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .formCuentasPorCobrar import *
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.db.models import Q,F,ExpressionWrapper,FloatField,Sum #para poder usar el operador | que funciona como OR
from datetime import timedelta
#from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
import pytz #para usar la zona horaria
import datetime #para que se pueda dar formato a la fecha
from decimal import *

def not_in_Caja_group(user):
    if user:
        return user.groups.filter(name='Caja').count() != 0
    return False

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def Abonos(request):
    if request.method=='POST':
        form_busquedas=Form_Abonos_busquedas(request.POST)
        form_Venta=Form_Abonos_Venta(request.POST)
        form_Cliente=Form_Abonos_Cliente(request.POST)
        form_persona=Form_Abonos_Persona(request.POST)
        form_PCC=Form_Abonos_PagosCuentasPorCobrar(request.POST)
        form_DetalleVenta=Form_Abonos_DetalleVenta(request.POST)
        form_DetalleVenta.fields["venta_idventa"].queryset = Venta.objects.filter(estado_venta=1)
    else:
        form_busquedas=Form_Abonos_busquedas()
        form_Venta=Form_Abonos_Venta()
        form_Cliente=Form_Abonos_Cliente()
        form_persona=Form_Abonos_Persona()
        form_PCC=Form_Abonos_PagosCuentasPorCobrar()
        form_DetalleVenta=Form_Abonos_DetalleVenta()
        form_DetalleVenta.fields["venta_idventa"].queryset = Venta.objects.filter(estado_venta=1)
    return render(request, 'kadoshapp/Abonos.html', {'form_DetalleVenta':form_DetalleVenta,'form_persona':form_persona,  'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_busquedas':form_busquedas,'form_PCC':form_PCC })

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def BuscarVentaAbono(request):
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
            fechainicial_real=fechainicial_real+datetime.timedelta(hours=6)
            fechafinal_real=fechafinal_real+datetime.timedelta(hours=6)
        resp_venta=Venta.objects.filter(Q(pk=int(cod_venta))|Q(cliente_idcliente__persona_idpersona__nombres_persona=nombres) | Q(cliente_idcliente__persona_idpersona__apellidos_persona=apellidos) | Q(cliente_idcliente__nit_cliente=nit )|Q(fecha_venta__range=(fechainicial_real,fechafinal_real)),estado_venta=1,es_cotizacion=0).values('pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona','fecha_venta','vendedor_venta__pk','empleado_idempleado__pk','total_venta','anotaciones_venta').order_by('pk')

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
def BuscarCuentaPorCobrar(request):
    if request.method == 'POST':
        cod_venta = request.POST.get('numeroventa')

        if not cod_venta:
            cod_venta=0
        cuenta=CuentaPorCobrar.objects.filter(venta_idventa=cod_venta).values('pk','venta_idventa__pk','saldo_inicial_cuentaporcobrar','saldo_actual_cuentaporcobrar')
        cuenta_diccionario=ValuesQuerySetToDict(cuenta)
        return HttpResponse(
            json.dumps(cuenta_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def BuscarPago(request):
    if request.method == 'POST':
        cod_cuenta = request.POST.get('numerocuenta')

        if not cod_cuenta:
            cod_cuenta=0
        pago=PagosCuentaPorCobrar.objects.filter(cuenta_por_cobrar_idcuenta_por_cobrar=cod_cuenta).values('pk','tipo_pago_idtipo_pago__nombre_tipopago','cuenta_por_cobrar_idcuenta_por_cobrar__pk','monto_pago_cuentaporcobrar','fecha_pago_cuentaporcobrar').order_by('pk')
        pago_diccionario=ValuesQuerySetToDict(pago)
        return HttpResponse(
            json.dumps(pago_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def GuardarPago(request):
    if request.method == 'POST':
        cod_cuenta = request.POST.get('numerocuenta')
        monto_pago = request.POST.get('montopago')
        tipo_pago = request.POST.get('tipopago')
        caja_pago = request.POST.get('cajapago')
        if not cod_cuenta:
            cod_cuenta=0
        if not tipo_pago:
            tipo_pago=0
        response_data={}
        try:
            obtenersaldo=CuentaPorCobrar.objects.filter(pk=cod_cuenta).values_list('saldo_actual_cuentaporcobrar',flat=True)[0]
            if Decimal(obtenersaldo)>=Decimal(monto_pago):
                nuevopago=PagosCuentaPorCobrar(cuenta_por_cobrar_idcuenta_por_cobrar=CuentaPorCobrar(pk=cod_cuenta),monto_pago_cuentaporcobrar=monto_pago,tipo_pago_idtipo_pago=TipoPago(pk=tipo_pago),caja_idcaja=Caja(pk=caja_pago))
                #verificar en el frontend que el monto del pago no sea mayor que el saldo inicial
                actualizarcuenta=CuentaPorCobrar.objects.filter(pk=cod_cuenta).update(saldo_actual_cuentaporcobrar=F('saldo_actual_cuentaporcobrar')-monto_pago)
                if actualizarcuenta: #solo si se actualizó la cuenta
                    response_data['nuevopago']=nuevopago.save()
                    response_data['actualizarcuenta']=actualizarcuenta
                if nuevopago and actualizarcuenta:
                    response_data['resultado']='Pago almacenado con éxito'
                else:
                    response_data['resultado']='No se almacenó el pago'
            else:
                response_data['resultado']='El monto del pago realizado es mayor al saldo actual'
        except Exception as e:
            response_data['resultado']='Error: ' + str(e)

        return HttpResponse(
            json.dumps(response_data,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def EntregarProducto(request):
    if request.method == 'POST':
        cod_venta = request.POST.get('numeroventa')
        cod_cuenta = request.POST.get('numerocuenta')
        response_data={}
        try:
            detalleventa=DetalleVenta.objects.filter(venta_idventa=Venta(pk=cod_venta)).values('inventario_producto_idinventario_producto__pk','cantidad_venta')
            detalleventa_diccionario=ValuesQuerySetToDict(detalleventa)
            for deta in detalleventa_diccionario:
                actualizarinventario=InventarioProducto.objects.filter(pk=deta['inventario_producto_idinventario_producto__pk']).update(existencia_actual=F('existencia_actual') - deta['cantidad_venta'])
            actualizarventa=Venta.objects.filter(pk=cod_venta).update(entregada_venta=1)
            response_data['resultado']='Producto entregado con éxito'
        except Exception as e:
            response_data['resultado']='Error: ' + str(e)    
        return HttpResponse(
            json.dumps(response_data,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )