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
@user_passes_test(not_in_AdministradorSistema_group, login_url='denegado') #linea para no permitir acceso al grupo
def reporte_apartados(request):
    if request.method == 'POST':
        reportedeudas=Venta.objects.filter(estado_venta=1,es_cotizacion=0,entregada_venta=0).values('pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona','total_venta','cuentaporcobrar__pk','cuentaporcobrar__saldo_inicial_cuentaporcobrar','cuentaporcobrar__saldo_actual_cuentaporcobrar')
        reporte1=ApartadosTabla(reportedeudas)
        RequestConfig(request).configure(reporte1)
    else:
        reportedeudas=Venta.objects.filter(estado_venta=1,es_cotizacion=0,entregada_venta=0).values('pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona','total_venta','cuentaporcobrar__pk','cuentaporcobrar__saldo_inicial_cuentaporcobrar','cuentaporcobrar__saldo_actual_cuentaporcobrar')
        reporte1=ApartadosTabla(reportedeudas)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
    return render(request,'kadoshapp/ReporteApartados.html',{'reporte1':reporte1})
