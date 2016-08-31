from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum, Count
from django.utils import timezone
import datetime
from django.db import connection
import pytz #para poder hacer la suma de los campos
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from .formReporteCompraEspecifica import *
def not_in_AdministradorSistema_group(user):
    if user:
        return user.groups.filter(name='AdministradorSistema').count() != 0
    return False

@login_required
@user_passes_test(not_in_AdministradorSistema_group, login_url='denegado')
def CompraEspecifica(request):
    if request.method == 'POST':
        form_compra=Form_CompraEspecifica_Busqueda(request.POST)
        if form_compra.is_valid():
            datosbusqueda=form_compra.cleaned_data
            numero=datosbusqueda['numerocompra']
            detallecompra=DetalleCompra.objects.filter(compra_idcompra=Compra(pk=numero)).values('pk',
                                                                                                 'cantidad_compra',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__pk',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__codigoestilo_producto',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__marca_id_marca__nombre_marca',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__estilo_idestilo__nombre_estilo',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__tipo_producto_idtipo_producto__nombre_tipoproducto',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__color_idcolor__nombre_color',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__talla_idtalla__nombre_talla',
                                                                                                 'inventario_producto_idinventario_producto__producto_codigo_producto__genero_idgener__nombre_genero',
                                                                                                 'valor_parcial_compra')
        reporte1=DetalleCompraTabla(detallecompra)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteCompraEspecifica.html',{'reporte1':reporte1,'form_compra':form_compra})
    else:
        form_compra=Form_CompraEspecifica_Busqueda()
        consulta=DetalleCompra.objects.all().values('pk',
                                                    'cantidad_compra',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__pk',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__codigoestilo_producto',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__marca_id_marca__nombre_marca',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__estilo_idestilo__nombre_estilo',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__tipo_producto_idtipo_producto__nombre_tipoproducto',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__color_idcolor__nombre_color',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__talla_idtalla__nombre_talla',
                                                    'inventario_producto_idinventario_producto__producto_codigo_producto__genero_idgener__nombre_genero',
                                                    'valor_parcial_compra')[:0]
        reporte1=DetalleCompraTabla(consulta)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReporteCompraEspecifica.html',{'reporte1':reporte1,'form_compra':form_compra})
