from django.conf.urls import include, url
from . import views
from . import ViewProducto,ViewTrabajador,viewReporteProductos,viewModificarCliente,viewAsignarCaja,viewListadoProductos,viewBusquedaMercaderia,viewPrecios,viewCliente, viewIngresoMercaPorProveedor, viewCompra, viewPuntodeVenta, viewTrasladoMercaderia, viewCierreCaja, viewAnularVenta, viewInventario, viewPromocion,viewEmpleados, viewCotizacion,viewModificarVenta,viewReporteCompras,viewReporteComprasExcel
from . import viewTablas
from . import viewReporteClientes,viewReporteClientesExcel
from . import ViewReporteVentas, ViewReporteVentasExcel
urlpatterns=[
#urls para loguear
url(r'^$','django.contrib.auth.views.login',
{'template_name':'kadoshapp/login.html'}, name='login'),

url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
url(r'^index/kadosh/', views.ingreso_mercaderia, name='ingreso_mercaderia'),
url(r'^Acceso/Denegado/', views.denegado, name='denegado'),
url(r'^ingreso/cliente/$', viewCliente.registro_cliente, name='registroCliente'),
url(r'^Registro/empleado/$', ViewTrabajador.registro_trabajador, name='registro_trabajador'),
url(r'^Elementos/Producto/$', ViewProducto.CosasProducto, name='Elementos'),
url(r'^modificar/cliente/$', viewModificarCliente.mod_cliente, name='modcliente'),
url(r'^ingreso/MercaderiaPoProveedor/$',viewIngresoMercaPorProveedor.ingresodemercaderiaporProveedor, name='IngresoMercaPorProveedor'),
url(r'^ingreso/Compra/$', viewCompra.Compra, name='Compra'),
url(r'^Realizacion/Venta/$', viewPuntodeVenta.PuntoDeVenta, name='PuntoDeVenta'),
url(r'^Traslado/Mercaderia/$', viewTrasladoMercaderia.TrasladoMercaderia, name='TrasladoMerca'),
url(r'^Cierre/Caja/$', viewCierreCaja.CierreDeCaja, name='CierreDeCaja'),
url(r'^Venta/Anular/$', viewAnularVenta.AnularVenta, name='AnularVenta'),
url(r'^Venta/Modificar/$', viewModificarVenta.ModificarVenta, name='ModificandoVenta'),
url(r'^Inventario/Nuevo/$', viewInventario.Inventario, name='Inventario'),
url(r'^Promocion/Nuevo/$', viewPromocion.Promocion, name='Promocion'),
url(r'^Buscar/Producto/$', viewPuntodeVenta.BuscarProducto, name='BusquedaProd'),
url(r'^Buscar/Producto/Traslado/$', viewTrasladoMercaderia.BuscarProducto, name='BusquedaProdTraslado'),
url(r'^Buscar/Producto/Precio/$', viewPrecios.BuscarProducto, name='BusquedaProdPrecio'),
url(r'^Buscar/Producto/Compra/$', viewCompra.BuscarProducto, name='BusquedaProdCompra'),
url(r'^Buscar/ProductoEstilo/Compra/$', viewCompra.BuscarProductoEstilo, name='BusquedaProdEstiloCompra'),
url(r'^Buscar/ProductoCaracteristicas/Compra/$', viewCompra.BuscarProductoCaracteristicas, name='BusquedaProdCompraCaracteristicas'),
url(r'^Buscar/Producto/ModificarVenta/$', viewModificarVenta.BuscarProductoDetalle, name='BusquedaProdModificarVenta'),
url(r'^Buscar/ProductoNuevo/ModificarVenta/$', viewModificarVenta.BuscarProductoNuevo, name='BusquedaProdNuevoModificarVenta'),
url(r'^Buscar/Precio/$', viewPrecios.BuscarPrecio, name='BusquedaPrecio'),
url(r'^Buscar/Venta/$', viewAnularVenta.BuscarVenta, name='BusquedaVenta'),
url(r'^Buscar/VentaModificar/$', viewModificarVenta.BuscarVenta, name='BusquedaVentaModificar'),
url(r'^Buscar/ProductoCaracteristicas/$', viewPuntodeVenta.BuscarProductoCaracteristicas, name='BusquedaProdCar'),
url(r'^Buscar/ProductoCaracteristicas/Traslado/$', viewTrasladoMercaderia.BuscarProductoCaracteristicas, name='BusquedaProdCarTraslado'),
url(r'^Buscar/ImagenProducto/$', viewPuntodeVenta.BuscarProductoImagenPrincipal, name='BusquedaProdImg'),
url(r'^Proveedor/AgregarObtener/$', viewCompra.GuardarObtenerProveedor, name='AgregarObtenerProveedor'),
url(r'^Anulacion/Venta/$', viewAnularVenta.AnulacionVenta, name='AnulacionVenta'),
url(r'^Modificacion/Venta/$', viewModificarVenta.ModificacionVenta, name='ModificacionVenta'),
url(r'^Empleados/Categoria/$', viewEmpleados.Empleados, name='Empleados'),
url(r'^Buscar/Empleados/$', viewEmpleados.BuscarEmpleados, name='BusquedaEmpleados'),
url(r'^Buscar/Cierre/$', viewCierreCaja.BuscarCaja, name='BusquedaCaja'),
url(r'^Buscar/ProductosInventario/$', viewInventario.BuscarProducto, name='BusquedaProductoInv'),
url(r'^Buscar/Cliente/$', viewModificarCliente.BuscarCliente, name='BusquedaCliente'),
url(r'^Buscar/DetalleVenta/$', viewModificarVenta.BuscarDetalleVenta, name='BusquedaDetalleVenta'),
url(r'^Buscar/ClienteEspecifico/$', viewModificarCliente.BuscarClienteEspecifico, name='BusquedaClienteEspecifico'),
url(r'^Cambiar/Puesto/$', viewEmpleados.CambiarPuestoEmpleado, name='PuestoEmpleados'),
url(r'^Asignar/Precio/$', viewPrecios.Precios, name='Precios'),
url(r'^Mercaderia/Busqueda/$', viewBusquedaMercaderia.BusquedaMerca, name='BusquedaMercaderia'),
url(r'^Subir/Imagen/$', viewCompra.SubirImagen, name='SubiendoImagen'),
url(r'^Productos/Listado/$', viewListadoProductos.Listado, name='ListadoProductos'),
url(r'^Registrar/Gasto/$', viewAsignarCaja.RegistrarGasto, name='RegitrarGasto'),
url(r'^Guardar/Venta/$', viewPuntodeVenta.GuardarVenta, name='GuardarVenta'),
url(r'^Guardar/Precio/$', viewPrecios.GuardarPrecio, name='GuardarPrecio'),
url(r'^Buscar/TodosProductosCaracteristicas/$', viewListadoProductos.BuscarProductoCaracteristicasExtra, name='BuscarListadoProductos'),
url(r'^Buscar/TodosProductosCaracteristicasExtra/$', viewListadoProductos.BuscarProductoCaracteristicasExtra, name='BuscarListadoProductos'),
url(r'^Buscar/TodosProductosExtra/$', viewListadoProductos.BuscarProductoExtra, name='BuscarListadoProductos'),
url(r'^Guardar/Venta/$', viewPuntodeVenta.GuardarVenta, name='GuardarVenta'),
#url(r'^reporte_personas_excel/$',viewReportePersonas.ReportePersonas.as_view(), name="reporte_personas_excel"),
#url(r'^Reporte/Personas/', viewTablas.persona_lista, name='Rpersonas'),
url(r'^cotizaciones/$',viewCotizacion.ReporteCotizacion.as_view(), name="reporte_cotizacion_excel"),
url(r'^reporte_productos_excel/$',viewReporteProductos.ReporteProductos.as_view(), name="reporte_productos_excel"),
url(r'^Reporte/Productos/', viewTablas.productos_lista, name='Rproductos'),
url(r'^Reporte/Clientes/', viewReporteClientes.Clientes, name='Rclientes'),
url(r'^Reporte/Compras/', viewReporteCompras.Compras, name='Rcompras'),
url(r'^reporte_clientes_excel/$',viewReporteClientesExcel.ReporteCliente.as_view(), name="reporte_clientes_excel"),
url(r'^Reporte/Ventas/', ViewReporteVentas.Ventas, name='RVentas'),
url(r'^reporte_ventas_excel/$',ViewReporteVentasExcel.ReporteVentas.as_view(), name="reporte_ventas_excel"),
url(r'^reporte_compras_excel/$',viewReporteComprasExcel.ReporteCompras.as_view(), name="reporte_compras_excel"),
]
