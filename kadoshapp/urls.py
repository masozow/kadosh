from django.conf.urls import include, url
from . import views
from . import viewReportePersonas,viewModificarCliente,viewAsignarCaja,viewListadoProductos,viewBusquedaMercaderia,viewPrecios,viewCliente, viewIngresoMercaPorProveedor, viewCompra, viewPuntodeVenta, viewTrasladoMercaderia, viewCierreCaja, viewAnularVenta, viewInventario, viewPromocion,viewEmpleados
from . import viewTablas
urlpatterns=[
#urls para loguear
url(r'^$','django.contrib.auth.views.login',
{'template_name':'kadoshapp/login.html'}, name='login'),

url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',
 name='logout'),
url(r'^index/kadosh/', views.ingreso_mercaderia, name='ingreso_mercaderia'),
url(r'^Acceso/Denegado/', views.denegado, name='denegado'),
url(r'^ingreso/cliente/$', viewCliente.registro_cliente, name='registroCliente'),
url(r'^modificar/cliente/$', viewModificarCliente.mod_cliente, name='modcliente'),
url(r'^ingreso/MercaderiaPoProveedor/$',viewIngresoMercaPorProveedor.ingresodemercaderiaporProveedor, name='IngresoMercaPorProveedor'),
url(r'^ingreso/Compra/$', viewCompra.Compra, name='Compra'),
url(r'^Realizacion/Venta/$', viewPuntodeVenta.PuntoDeVenta, name='PuntoDeVenta'),
url(r'^Traslado/Mercaderia/$', viewTrasladoMercaderia.TrasladoMercaderia, name='TrasladoMerca'),
url(r'^Cierre/Caja/$', viewCierreCaja.CierreDeCaja, name='CierreDeCaja'),
url(r'^Venta/Anular/$', viewAnularVenta.AnularVenta, name='AnularVenta'),
url(r'^Inventario/Nuevo/$', viewInventario.Inventario, name='Inventario'),
url(r'^Promocion/Nuevo/$', viewPromocion.Promocion, name='Promocion'),
url(r'^Buscar/Producto/$', viewPuntodeVenta.BuscarProducto, name='BusquedaProd'),
url(r'^Buscar/ProductoCaracteristicas/$', viewPuntodeVenta.BuscarProductoCaracteristicas, name='BusquedaProdCar'),
url(r'^Buscar/ImagenProducto/$', viewPuntodeVenta.BuscarProductoImagenPrincipal, name='BusquedaProdImg'),
url(r'^Empleados/Categoria/$', viewEmpleados.Empleados, name='Empleados'),
url(r'^Buscar/Empleados/$', viewEmpleados.BuscarEmpleados, name='BusquedaEmpleados'),
url(r'^Cambiar/Puesto/$', viewEmpleados.CambiarPuestoEmpleado, name='PuestoEmpleados'),
url(r'^Asignar/Precio/$', viewPrecios.Precios, name='Precios'),
url(r'^Mercaderia/Busqueda/$', viewBusquedaMercaderia.BusquedaMerca, name='BusquedaMercaderia'),
url(r'^Productos/Listado/$', viewListadoProductos.Listado, name='ListadoProductos'),
url(r'^Asignar/Caja/$', viewAsignarCaja.Asignacion, name='AsignarCaja'),
url(r'^Guardar/Venta/$', viewPuntodeVenta.GuardarVenta, name='GuardarVenta'),
url(r'^Buscar/TodosProductosCaracteristicas/$', viewListadoProductos.BuscarProductoCaracteristicasExtra, name='BuscarListadoProductos'),
url(r'^reporte_personas_excel/$',viewReportePersonas.ReportePersonas.as_view(), name="reporte_personas_excel"),
url(r'^Guardar/Venta/$', viewPuntodeVenta.GuardarVenta, name='GuardarVenta'),
url(r'^reporte_personas_excel/$',viewReportePersonas.ReportePersonas.as_view(), name="reporte_personas_excel"),
url(r'^Reporte/Personas/', viewTablas.persona_lista, name='Rpersonas'),
]
