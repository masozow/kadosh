from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime, timedelta
#from dateutil.relativedelta import relativedelta
from django.db import connection
import pytz #para poder hacer la suma de los campos
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

@login_required
def Resumenes(request):
    if request.method == 'POST':
        fecha=timezone.now()
        vendedores=Venta.objects.filter(vendedor_venta__puesto_idpuesto__nombre_puesto__contains='Ventas',vendedor_venta__estado_empleado=1,fecha_venta__month=fecha.month,fecha_venta__year=fecha.year).values('vendedor_venta__pk','vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona','vendedor_venta__puesto_idpuesto__nombre_puesto').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')
        productos=Venta.objects.filter(fecha_venta__lte=fecha2).filter(detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__estado_producto=1).values('detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__pk','detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto','detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__codigobarras_producto','detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__codigoestilo_producto','fecha_venta')
        reporteproductos=ProductosSinMovimientoTabla(productos)
        reportevendedores=VendedoresPuestoTabla(vendedores)
        RequestConfig(request, paginate={'per_page': 25}).configure(reportevendedores)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporteproductos)
        return render(request,'kadoshapp/Resumenes.html',{'reportevendedores':reportevendedores,'reporteproductos':reporteproductos})
    else:
        fecha=timezone.now()
        fecha2= fecha - timedelta(3*365/12)
        vendedores=Venta.objects.filter(vendedor_venta__puesto_idpuesto__nombre_puesto__contains='Ventas',vendedor_venta__estado_empleado=1,fecha_venta__year=fecha.year,fecha_venta__month=fecha.month).values('vendedor_venta__pk','vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona','vendedor_venta__puesto_idpuesto__nombre_puesto').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')
        productos=Venta.objects.filter(fecha_venta__lte=fecha2).filter(detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__estado_producto=1).values('detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__pk','detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto','detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__codigobarras_producto','detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__codigoestilo_producto','fecha_venta')
        reporteproductos=ProductosSinMovimientoTabla(productos)
        reportevendedores=VendedoresPuestoTabla(vendedores)
        RequestConfig(request, paginate={'per_page': 25}).configure(reportevendedores)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporteproductos)
        return render(request,'kadoshapp/Resumenes.html',{'reportevendedores':reportevendedores,'reporteproductos':reporteproductos})
