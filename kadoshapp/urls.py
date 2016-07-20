from django.conf.urls import include, url
from . import views

urlpatterns=[
#urls para loguear
url(r'^$','django.contrib.auth.views.login',
{'template_name':'kadoshapp/login.html'}, name='login'),

url(r'^$','django.contrib.auth.views.logout_then_login',
 name='logout'),
url(r'^index/kadosh/', views.ingreso_mercaderia, name='ingreso_mercaderia'),
url(r'^ingreso/cliente/$', views.registro_cliente, name='registroCliente'),
url(r'^ingreso/MercaderiaPoProveedor/$', views.ingresodemercaderiaporProveedor, name='IngresoMercaPorProveedor'),
url(r'^ingreso/Compra/$', views.Compra, name='Compra'),
url(r'^Realizacion/Venta/$', views.PuntoDeVenta, name='PuntoDeVenta'),
url(r'^Trazalado/Mercaderia/$', views.TrasladoMercaderia, name='TrasladoMerca'),
url(r'^Cierre/Caja/$', views.CierreDeCaja, name='CierreDeCaja'),
url(r'^Venta/Anular/$', views.AnularVenta, name='AnularVenta'),
url(r'^Inventario/Nuevo/$', views.Inventario, name='Inventario'),
url(r'^Promocion/Nuevo/$', views.Promocion, name='Promocion'),
]
