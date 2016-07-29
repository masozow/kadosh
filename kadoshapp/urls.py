from django.conf.urls import include, url
from . import views
from . import viewCliente, viewIngresoMercaPorProveedor, viewCompra, viewPuntodeVenta, viewTrasladoMercaderia, viewCierreCaja, viewAnularVenta, viewInventario, viewPromocion

urlpatterns=[
#urls para loguear
url(r'^$','django.contrib.auth.views.login',
{'template_name':'kadoshapp/login.html'}, name='login'),

url(r'^$','django.contrib.auth.views.logout_then_login',
 name='logout'),
url(r'^index/kadosh/', views.ingreso_mercaderia, name='ingreso_mercaderia'),
url(r'^ingreso/cliente/$', viewCliente.registro_cliente, name='registroCliente'),
url(r'^ingreso/MercaderiaPoProveedor/$',viewIngresoMercaPorProveedor.ingresodemercaderiaporProveedor, name='IngresoMercaPorProveedor'),
url(r'^ingreso/Compra/$', viewCompra.Compra, name='Compra'),
url(r'^Realizacion/Venta/$', viewPuntodeVenta.PuntoDeVenta, name='PuntoDeVenta'),
url(r'^Trazalado/Mercaderia/$', viewTrasladoMercaderia.TrasladoMercaderia, name='TrasladoMerca'),
url(r'^Cierre/Caja/$', viewCierreCaja.CierreDeCaja, name='CierreDeCaja'),
url(r'^Venta/Anular/$', viewAnularVenta.AnularVenta, name='AnularVenta'),
url(r'^Inventario/Nuevo/$', viewInventario.Inventario, name='Inventario'),
url(r'^Promocion/Nuevo/$', viewPromocion.Promocion, name='Promocion'),
url(r'^Buscar/Producto/$', viewPuntodeVenta.BuscarProducto, name='BusquedaProd'),
]
