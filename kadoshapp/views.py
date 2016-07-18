from django.shortcuts import render
from .models import Persona, Cliente, TipoCliente
from .forms import Form_RegistroCliente_Persona, Form_RegistroCliente_Cliente
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
#importacion para form de IngresoMercaderiaPorProveedor
from .models import Producto, DetalleCompra, TipoProducto, Fotografia, InventarioProducto, Anaquel, Compra
from .forms import Form_IngresoMercaderiaPorProveedor_Producto, Form_IngresoMercaderiaPorProveedor_DetalleCompra, Form_IngresoMercaderiaPorProveedor_TipoProducto, Form_IngresoMercaderiaPorProveedor_Fotografia, Form_IngresoMercaderiaPorProveedor_InventarioProducto, Form_IngresoMercaderiaPorProveedor_Anaquel, Form_IngresoMercaderiaPorProveedor_Compra
#cosas de form Compra
from .models import Compra, InventarioProducto, Producto, DetalleCompra, Fotografia, Anaquel, TipoProducto
from .forms import Form_Compra_Compra, Form_Compra_InventarioProducto,Form_Compra_Producto, Form_Compra_DetalleCompra,Form_Compra_Fotografia, Form_Compra_Anaquel, Form_Compra_TipoProducto
#cosas de punto de Venta
from .models import Venta, DetalleVenta, InventarioProducto, TipoProducto, Producto, Promocion, Precio
from .forms import Form_PuntoVenta_Venta,Form_PuntoVenta_DetalleVenta,Form_PuntoVenta_InventarioProducto, Form_PuntoVenta_TipoProducto, Form_PuntoVenta_Producto, Form_PuntoVenta_Promocion,Form_PuntoVenta_Precio, Form_PuntoVenta_busquedas, Form_PuntoVenta_EstiloProducto, Form_PuntoVenta_PromocionHasProducto
#cosas Traslado de mercaderia
from .models import TrasladoMercaderia, Producto, TipoProducto, InventarioProducto
from .forms import Form_TrasladoMerca_TrasaladoMercaderia, Form_TrasladoMerca_Producto, Form_TrasladoMerca_TipoProducto, Form_TrasladoMerca_InventarioProducto, Form_TrasladoMerca_Cantidad
#impor para formulario de CierreDeCaja
from .models import CierreDeCaja, Empleado
from .forms import Form_CierreDeCaj_CierreDeCaja, Form_CierreDeCaj_Empleado
#cosas Anular Venta
from .models import Venta, Cliente, DetalleVenta, Empleado
from .forms import Form_AnulaVenta_Venta, Form_AnulaVenta_Cliente, Form_AnulaVenta_DetalleVenta, Form_AnulaVenta_Empleado
#cosar para Inventario
from .models import Empleado, Anaquel, InventarioProducto, DetalleInventarioRealizado, AjusteInventario, InventarioRealizado
from .forms import Form_Inventario_InventarioRealizado, Form_Inventario_Empleado,Form_Inventario_InventarioProducto, Form_Inventario_Anque, Form_Inventario_InventarioProducto, Form_Inventario_DetalleInventarioRealizado, Form_Inventario_AjusteInventario
#cosas de Promocion
from .models import Producto, TipoProducto, InventarioProducto, Promocion
from .forms import Form_Promocion_Producto, form_Promocion_TipoProducto, Form_Promocion_InventarioProducto, Form_Promocion_Promocion, form_Promocion_Cantidad


# Creat your views here.
def ingreso_mercaderia(request):
    return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
#Vista de Promocion
def Promocion(request):
    if request.method=='POST':
        form_promocion=Form_Promocion_Promocion(request.POST)
        if form_promocion.is_valid():
            ultima_promocion=form_promocion.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_promocion=Form_Promocion_Promocion()
        form_producto=Form_Promocion_Producto()
        form_tipoproducto=form_Promocion_TipoProducto()
        form_inventarioproducto=Form_Promocion_InventarioProducto()
        form_cantidad=form_Promocion_Cantidad()
    return render(request, 'kadoshapp/Promocion.html', {'form_promocion':form_promocion, 'form_producto':form_producto, 'form_tipoproducto':form_tipoproducto, 'form_inventarioproducto':form_inventarioproducto , 'form_cantidad':form_cantidad  })


#vista CierreDeCaja
def Inventario(request):
    if request.method=='POST':
        form_Invetario=Form_Inventario_InventarioProducto(request.POST)
        if form_inventario.is_valid():
            ultimo_invenario=form_inventario.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_inventario=Form_TrasladoMerca_InventarioProducto()
        form_anaquel=Form_Inventario_Anque()
        form_detallainventario=Form_Inventario_DetalleInventarioRealizado()
        form_empleado=Form_Inventario_Empleado()
        form_ajusteinventario=Form_Inventario_AjusteInventario()
        form_inventariorealizado=Form_Inventario_InventarioRealizado();
    return render(request, 'kadoshapp/Inventario.html', {'form_inventario':form_inventario, 'form_anaquel':form_anaquel, 'form_detallainventario':form_detallainventario, 'form_empleado':form_empleado , 'form_ajusteinventario':form_ajusteinventario, 'form_inventariorealizado':form_inventariorealizado  })



#vista CierreDeCaja
def AnularVenta(request):
    if request.method=='POST':
        form_Venta=Form_AnulaVenta_Venta(request.POST)
        if form_Venta.is_valid():
            ultima_anulacionventa=form_Venta.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Venta=Form_AnulaVenta_Venta()
        form_Cliente=Form_AnulaVenta_Cliente()
        form_DetalleVenta=Form_AnulaVenta_DetalleVenta()
        form_empleado=Form_AnulaVenta_Empleado()
    return render(request, 'kadoshapp/AnularVenta.html', {'form_Venta':form_Venta, 'form_Cliente':form_Cliente, 'form_DetalleVenta':form_DetalleVenta, 'form_empleado':form_empleado })


#vista CierreDeCaja
def CierreDeCaja(request):
    if request.method=='POST':
        form_Cierrecaja=Form_CierreDeCaj_CierreDeCaja(request.POST)
        if form_Cierrecaja.is_valid():
            ultimo_cierre=form_Cierrecaja.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Cierrecaja=Form_CierreDeCaj_CierreDeCaja()
        form_empleado=Form_CierreDeCaj_Empleado()

    return render(request, 'kadoshapp/CierreDeCaja.html', {'form_Cierrecaja':form_Cierrecaja,'form_empleado':form_empleado })



#CVista de Traslado de mercaderia
def TrasladoMercaderia(request):
    if request.method=='POST':
        form_Traslado=Form_TrasladoMerca_TrasaladoMercaderia(request.POST)
        if form_Traslado.is_valid():
            ultimo_traslado=form_Traslado.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Traslado=Form_TrasladoMerca_TrasaladoMercaderia()
        form_Producto=Form_TrasladoMerca_Producto
        form_TipoProducto=Form_TrasladoMerca_TipoProducto
        form_InventarioProducto=Form_TrasladoMerca_InventarioProducto
        form_cantidad=Form_TrasladoMerca_Cantidad
    return render(request, 'kadoshapp/TrasladoMerca.html', {'form_TipoProducto':form_TipoProducto,'form_Producto':form_Producto ,'form_InventarioProducto':form_InventarioProducto, 'form_Traslado':form_Traslado, 'form_cantidad':form_cantidad })


#Vista de Punto de Venta
def PuntoDeVenta(request):
    if request.method=='POST':
        #form_Venta=Form_PuntoVenta_Venta(request.POST)
        #if form_Venta.is_valid():
        #    ultima_venta=form_Venta.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Venta=Form_PuntoVenta_Venta()
        form_DetalleVenta=Form_PuntoVenta_DetalleVenta()
        form_InventarioProducto=Form_PuntoVenta_InventarioProducto()
        form_Producto=Form_PuntoVenta_Producto()
        form_TipoProducto=Form_PuntoVenta_TipoProducto()
        form_Promocion=Form_PuntoVenta_Promocion()
        form_Precio=Form_PuntoVenta_Precio()
        form_cliente=Form_PuntoVenta_busquedas()
        form_estiloproducto=Form_PuntoVenta_EstiloProducto()
        form_promocionhasproducto=Form_PuntoVenta_PromocionHasProducto()
    return render(request, 'kadoshapp/PuntoDeVenta.html', {
                    'form_Venta': form_Venta,
                    'form_DetalleVenta':form_DetalleVenta,
                    'form_TipoProducto':form_TipoProducto,
                    'form_Producto':form_Producto ,
                    'form_InventarioProducto':form_InventarioProducto,
                    'form_Promocion':form_Promocion, 'form_Precio':form_Precio,
                    'form_cliente':form_cliente,
                    'form_estiloproducto':form_estiloproducto,
                    'form_promocionhasproducto': form_promocionhasproducto
                    })




#Vista de form de compra
def Compra(request):
    if request.method=='POST':
        form_Compra=Form_Compra_Compra(request.POST)
        if form_Compra.is_valid():
            ultima_Compra=form_Compra.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Compra=Form_Compra_Compra()
        form_Detallecompra=Form_Compra_DetalleCompra()
        form_InventarioProducto=Form_Compra_InventarioProducto()
        form_Producto=Form_Compra_Producto()
        form_fotografia=Form_Compra_Fotografia()
        form_anaquel=Form_Compra_Anaquel()
        form_TipoProducto=Form_Compra_TipoProducto()
    return render(request, 'kadoshapp/Compra.html', {'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto, 'form_anaquel':form_anaquel, 'form_Compra':form_Compra })



#Vista de formulario de IngresoDeMercaderiaPorProveedor
def ingresodemercaderiaporProveedor(request):
    if request.method=='POST':
        form_Producto=Form_IngresoMercaderiaPorProveedor_Producto(request.POST)
        if form_Producto.is_valid():
            ultimo_producto=form_Producto.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Producto=Form_IngresoMercaderiaPorProveedor_Producto()
        form_Detallecompra=Form_IngresoMercaderiaPorProveedor_DetalleCompra()
        form_TipoProducto=Form_IngresoMercaderiaPorProveedor_TipoProducto()
        form_fotografia=Form_IngresoMercaderiaPorProveedor_Fotografia()
        form_InventarioProducto=Form_IngresoMercaderiaPorProveedor_InventarioProducto()
        form_anaquel=Form_IngresoMercaderiaPorProveedor_Anaquel()
        form_Compra=Form_IngresoMercaderiaPorProveedor_Compra()
    return render(request, 'kadoshapp/IngresoMercaderiaPorProveedor.html', {'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto, 'form_anaquel':form_anaquel, 'form_Compra':form_Compra })



def registro_cliente(request):
    if request.method == 'POST':
        form=Form_RegistroCliente_Persona(request.POST)
        if form.is_valid(): #validando a la persona
            ultima_persona=form.save()
            #return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
        else:
            print (f.errors)
            #mensaje error (raise error)
        sub_form=Form_RegistroCliente_Cliente(request.POST)
                #ultima_persona=Persona.objects.order_by('-idpersona')[:1]
                #[:1] es el equivalente de SQL a: TOP 1.
                #El - antes del nombre del campo indica que es en orden descendente
        if sub_form.is_valid():
            sf=sub_form.save(commit=False)
            #aqui solo se guarda el objeto del formulario del cliente en la variable sf
            #se le indica que no haga el commit para que aún no lo guarde en la BD
            sf.persona_idpersona=ultima_persona
            #se accede al campo persona_idpersona del modelo Cliente,
            #que se encuentra ya en el formulario, para cambiar su valor
            #por el que devuelve el queryset ultima_persona
            sf.save()
            #ahora sí se guarda
        else:
            print (sf.errors)
            #mensaje error (raise error)
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form=Form_RegistroCliente_Persona()
        sub_form=Form_RegistroCliente_Cliente()
    return render(request, 'kadoshapp/Datos_cliente.html', {'form': form, 'sub_form':sub_form})
