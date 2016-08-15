from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.contrib.auth.decorators import login_required
#para tablas
from django_tables2 import RequestConfig
from .models import Persona
from .tables import PersonaTabla
#from .models import Persona, Cliente, TipoCliente
#from .forms import Form_RegistroCliente_Persona, Form_RegistroCliente_Cliente
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
#importacion para form de IngresoMercaderiaPorProveedor
#from .models import Producto, DetalleCompra, TipoProducto, Fotografia, InventarioProducto, Anaquel, Compra
#from .forms import Form_IngresoMercaderiaPorProveedor_Producto, Form_IngresoMercaderiaPorProveedor_DetalleCompra, Form_IngresoMercaderiaPorProveedor_TipoProducto, Form_IngresoMercaderiaPorProveedor_Fotografia, Form_IngresoMercaderiaPorProveedor_InventarioProducto, Form_IngresoMercaderiaPorProveedor_Anaquel, Form_IngresoMercaderiaPorProveedor_Compra
#cosas de form Compra
#from .models import Compra, InventarioProducto, Producto, DetalleCompra, Fotografia, Anaquel, TipoProducto
#from .forms import Form_Compra_Compra, Form_Compra_InventarioProducto,Form_Compra_Producto, Form_Compra_DetalleCompra,Form_Compra_Fotografia, Form_Compra_Anaquel, Form_Compra_TipoProducto
#cosas de punto de Venta
#from .models import Venta, DetalleVenta, InventarioProducto, TipoProducto, Producto, Promocion, Precio
#from .forms import Form_PuntoVenta_Venta,Form_PuntoVenta_DetalleVenta,Form_PuntoVenta_InventarioProducto, Form_PuntoVenta_TipoProducto, Form_PuntoVenta_Producto, Form_PuntoVenta_Promocion,Form_PuntoVenta_Precio, Form_PuntoVenta_busquedas, Form_PuntoVenta_EstiloProducto, Form_PuntoVenta_PromocionHasProducto
#cosas Traslado de mercaderia
#from .models import TrasladoMercaderia, Producto, TipoProducto, InventarioProducto
#from .forms import Form_TrasladoMerca_TrasaladoMercaderia, Form_TrasladoMerca_Producto, Form_TrasladoMerca_TipoProducto, Form_TrasladoMerca_InventarioProducto, Form_TrasladoMerca_Cantidad
#impor para formulario de CierreDeCaja
#from .models import CierreDeCaja, Empleado
#from .forms import Form_CierreDeCaj_CierreDeCaja, Form_CierreDeCaj_Empleado
#cosas Anular Venta
#from .models import Venta, Cliente, DetalleVenta, Empleado
#from .forms import Form_AnulaVenta_Venta, Form_AnulaVenta_Cliente, Form_AnulaVenta_DetalleVenta, Form_AnulaVenta_Empleado
#cosar para Inventario
#from .models import Empleado, Anaquel, InventarioProducto, DetalleInventarioRealizado, AjusteInventario, InventarioRealizado
#from .forms import Form_Inventario_InventarioRealizado, Form_Inventario_Empleado,Form_Inventario_InventarioProducto, Form_Inventario_Anque, Form_Inventario_InventarioProducto, Form_Inventario_DetalleInventarioRealizado, Form_Inventario_AjusteInventario
#cosas de Promocion
#from .models import Producto, TipoProducto, InventarioProducto, Promocion
#from .forms import Form_Promocion_Producto, form_Promocion_TipoProducto, Form_Promocion_InventarioProducto, Form_Promocion_Promocion, form_Promocion_Cantidad


# Creat your views here.
@login_required
def ingreso_mercaderia(request):
    return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
@login_required
def denegado(request):
    return render(request, 'kadoshapp/Denegado.html',{})
