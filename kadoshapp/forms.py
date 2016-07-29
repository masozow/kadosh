from django import forms
from django.forms import ModelChoiceField,Select
from django.contrib.admin import widgets
from django.forms import extras

from .formclientes import *
from .formIngresoMercaPorProveedor import *
from .models import *
#Import para formulario de Ingres de mercaderia por Proveedor
#from .models import Producto, DetalleCompra, TipoProducto, Fotografia, InventarioProducto, Anaquel, Compra
#Import para formulario de Compra
#from .models import Anaquel #, TipoProducto, Producto, Compra, InventarioProducto, DetalleCompra, Fotografia,
#impor para formulario de Punto de Venta
#from .models import Venta, DetalleVenta, Promocion, Precio,Estilo, PromocionHasProducto #'''TipoProducto,''' InventarioProducto, Producto,
#import para formulario de Traslado de mercaderia
#from .models import TrasladoMercaderia #'''TipoProducto''', , Producto, InventarioProducto
#impor para formulario de CierreDeCaja
#from .models import CierreDeCaja, Empleado
#impor para formulario Anular Venta
#from .models import Venta, Cliente, DetalleVenta, Empleado
#import para formulario Inventario
#from .models import DetalleInventarioRealizado, AjusteInventario, InventarioRealizado #Empleado, Anaquel, InventarioProducto,
#import para formulario de Promocion
#from .models import Promocion #'''Producto, TipoProducto,InventarioProducto, '''
