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
        txt_codigo_producto = request.POST.get('codigoestilo_producto')
        id_marca_producto = request.POST.get('marca_id_marca')
        id_estilo_producto = request.POST.get('estilo_idestilo')
        id_tipo_producto = request.POST.get('tipo_producto_idtipo_producto')
        id_talla_producto = request.POST.get('talla_idtalla')
        id_color_producto = request.POST.get('color_idcolor')
        id_genero_producto = request.POST.get('genero_idgener')
        txt_codigo_barras= request.POST.get('codigobarras_producto')
         #el not indica que la cadena está vacía, o que la variable es null
        if not id_marca_producto:
            id_marca_producto=0
        if not id_estilo_producto:
            id_estilo_producto=0
        if not id_tipo_producto:
            id_tipo_producto=0
        if not id_talla_producto:
            id_talla_producto=0
        if not id_color_producto:
            id_color_producto=0
        if not id_genero_producto:
            id_genero_producto=0


        if txt_codigo_producto and id_marca_producto !=0 and id_estilo_producto !=0 and id_tipo_producto !=0 and id_talla_producto !=0 and id_color_producto != 0 and id_genero_producto !=0:
            resultado_caracteristicas=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,estilo_idestilo=id_estilo_producto,tipo_producto_idtipo_producto=id_tipo_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #todos los parametros
        elif txt_codigo_producto and id_marca_producto !=0 and id_tipo_producto !=0 and id_talla_producto !=0 and id_color_producto != 0 and id_genero_producto !=0:
            resultado_caracteristicas=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,tipo_producto_idtipo_producto=id_tipo_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo
        elif txt_codigo_producto and id_marca_producto !=0 and id_talla_producto !=0 and id_color_producto != 0 and id_genero_producto !=0:
            resultado_caracteristicas=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo
        elif txt_codigo_producto and id_marca_producto !=0 and id_talla_producto !=0 and id_genero_producto !=0:
            resultado_caracteristicas=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,talla_idtalla=id_talla_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color
        elif txt_codigo_producto and id_marca_producto !=0 and id_genero_producto !=0:
            resultado_caracteristicas=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla
        elif txt_codigo_producto and id_marca_producto !=0:
            resultado_caracteristicas=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla, sin genero
        elif id_marca_producto !=0:
            resultado_caracteristicas=Producto.objects.filter(marca_id_marca=id_marca_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla, sin genero, sin codigo estilo
        elif txt_codigo_producto:
            resultado_caracteristicas=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla, sin genero, sin marca, sin codigo barras
        elif txt_codigo_barras:
            resultado_caracteristicas=Producto.objects.filter(codigobarras_producto=txt_codigo_barras,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla, sin genero, sin marca, sin codigo estilo
        else:
            resultado_caracteristicas=Producto.objects.filter(Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto),inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            if not resultado_caracteristicas:
                resultado_caracteristicas=Producto.objects.filter(inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))


        #if not txt_codigo_producto and not txt_codigo_barras  and id_marca_producto==0 and id_estilo_producto==0 and id_tipo_producto==0 and id_talla_producto==0 and id_color_producto==0 and id_genero_producto==0:
			#Cuando todos los parámetros van vacíos
        #    resultado_caracteristicas=Producto.objects.filter(inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
        #else:
		   #Cuando existe por lo menos un parámetro (los números dentro de filter deben reemplazarse por los parámetros que envía el usuario)
        #    resultado_caracteristicas=Producto.objects.filter(Q(codigobarras_producto=txt_codigo_barras)|Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto),inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))


        #form_producto=Form_Busqueda_Producto()
        reporte1=ProductosTabla(resultado_caracteristicas)
        RequestConfig(request).configure(reporte1)
        return render(request,'kadoshapp/ReporteProductos.html',{'reporte1':reporte1,'form_producto':form_producto})
    else:
        form_producto=Form_Busqueda_Producto()
        consulta=Producto.objects.filter(inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
        reporte1=ProductosTabla(consulta)
        #RequestConfig(request).configure(reporte1)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteProductos.html',{'reporte1':reporte1,'form_producto':form_producto})
