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
from .formReporteClientes import *
@login_required

def Resumenes(request):
    if request.method == 'POST':
        #reporte1=ClientesTabla(compras_clientes)
        #RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReportesClientes.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_cliente':form_cliente,'form_check':form_check})
    else:
        fecha=datetime.datetime.today()
        fecha2= fecha + datetime.timedelta(days=2)
        #anio=fecha.year
        #posts = TodaysObject.objects.extra([where='DAY(publish_date)<=%d AND MONTH(publish_date)=%d' % (now.day, now.month)])
        clientes=Cliente.objects.filter(persona_idpersona__fecha_nacimiento_persona__range=(fecha,fecha2))
        Venta.objects.filter(), datetime.datetime(int(fecha2_split[2]),int(fecha2_split[1]), int(fecha2_split[0]),23,59,59,tzinfo=pytz.UTC))).values('cliente_idcliente__nit_cliente','cliente_idcliente__pk','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona').annotate(total_ventas=Sum('total_venta')).order_by('total_ventas')
        form_fecha=Form_Busqueda_Fechas()
        form_cliente=Form_Busqueda_Cliente()
        form_check=Form_Busqueda_Checbox()
        consulta=Cliente.objects.all()
        reporte1=ClientesTabla(consulta)
        RequestConfig(request, paginate={'per_page': 25}).configure(reporte1)
        return render(request,'kadoshapp/ReportesClientes.html',{'reporte1':reporte1,'form_fecha':form_fecha,'form_cliente':form_cliente,'form_check':form_check})
