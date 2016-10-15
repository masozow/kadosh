from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum #para poder hacer la suma de los campos
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from .formBusquedaMercaderia import *
def not_in_AdministradorSistema_group(user):
    if user:
        return user.groups.filter(name='AdministradorSistema').count() != 0
    return False
@login_required
@user_passes_test(not_in_AdministradorSistema_group, login_url='denegado')
def productos_lista(request):
    if request.method == 'POST':
        form_producto=Form_Busqueda_Producto(request.POST)

        resp_producto=Producto.objects.filter(inventarioproducto__detalleventa__venta_idventa__entregada_venta=1,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
        txt_codigo_barras = request.POST.get('codigobarras_producto')
        if txt_codigo_barras:
            resp_producto=resp_producto.filter(codigobarras_producto=txt_codigo_barras)
        else:
            txt_codigo_producto = request.POST.get('codigoestilo_producto')
            if txt_codigo_producto:
                resp_producto=resp_producto.filter(codigoestilo_producto=txt_codigo_producto)
            
            id_marca_producto = request.POST.get('marca_id_marca')
            if id_marca_producto:
                resp_producto=resp_producto.filter(marca_id_marca=id_marca_producto)

            id_estilo_producto = request.POST.get('estilo_idestilo')
            if id_estilo_producto:
                resp_producto=resp_producto.filter(estilo_idestilo=id_estilo_producto)

            id_tipo_producto = request.POST.get('tipo_producto_idtipo_producto')
            if id_tipo_producto:
                resp_producto=resp_producto.filter(tipo_producto_idtipo_producto=id_tipo_producto)

            id_talla_producto = request.POST.get('talla_idtalla')
            if id_talla_producto:
                resp_producto=resp_producto.filter(talla_idtalla=id_talla_producto)

            id_color_producto = request.POST.get('color_idcolor')
            if id_color_producto:
                resp_producto=resp_producto.filter(color_idcolor=id_color_producto)

            id_genero_producto = request.POST.get('genero_idgener')
            if id_genero_producto:
                resp_producto=resp_producto.filter(genero_idgener=id_genero_producto)

        #form_producto=Form_Busqueda_Producto()
        reporte1=ProductosTabla(resp_producto)
        RequestConfig(request).configure(reporte1)
    else:
        form_producto=Form_Busqueda_Producto()
        consulta=Producto.objects.filter(inventarioproducto__detalleventa__venta_idventa__entregada_venta=1,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
        reporte1=ProductosTabla(consulta)
        #RequestConfig(request).configure(reporte1)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
    return render(request,'kadoshapp/ReporteProductos.html',{'reporte1':reporte1,'form_producto':form_producto})
