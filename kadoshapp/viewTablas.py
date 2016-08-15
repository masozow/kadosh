from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import ProductosTabla
from django.contrib.auth.decorators import login_required, user_passes_test
@login_required
def productos_lista(request):
    reporte1 = ProductosTabla(Producto.objects.filter(codigobarras_producto=123).values('pk',
                                                                                           'nombre_producto',
                                                                                           'inventarioproducto__bodega_idbodega__nombre_bodega',
                                                                                           'codigobarras_producto',
                                                                                           'inventarioproducto__existencia_actual',
                                                                                           'codigoestilo_producto',
                                                                                           'precio__valor_precio',
                                                                                           'marca_id_marca__nombre_marca'))
    RequestConfig(request).configure(reporte1)
    return render(request,'kadoshapp/ReporteProductos.html',{'reporte1':reporte1})
