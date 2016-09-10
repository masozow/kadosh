from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
#import pdb #para hacer el debugging
#from .models import Persona, Cliente, TipoCliente
#from .forms import Form_RegistroCliente_Persona, Form_RegistroCliente_Cliente
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
#from django_tables2 import RequestConfig
from .models import *
#from .tables import *
#from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum, Count
#from django.utils import timezone
#import datetime
#from datetime import datetime, timedelta
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
#from django.db.models import Q #para poder usar el operador | que funciona como OR
#from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

# Creat your views here.
def productos(request):
    productos_mostrar=ProductoHasFotografia.objects.filter(fotografia_idfotografia__principal_fotografia=1,fotografia_idfotografia__estado_fotografia=1,producto_codigo_producto__estado_producto=1,producto_codigo_producto__publicar_producto=1,producto_codigo_producto__oferta_producto=0).annotate(total=Count('producto_codigo_producto')).values('producto_codigo_producto__pk','producto_codigo_producto__nombre_producto','producto_codigo_producto__descripcion_producto','fotografia_idfotografia__pk','fotografia_idfotografia__ruta_fotografia','producto_codigo_producto__marca_id_marca__nombre_marca').order_by('producto_codigo_producto__nombre_producto')
    marcas=Marca.objects.filter(estado_marca=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    generos=Genero.objects.filter(estado_genero=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    tipos=TipoProducto.objects.filter(estado_tipoproducto=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    return render(request,'kadoshapp/WEBproductos.html',{'productos':productos_mostrar,'marcas':marcas,'generos':generos,'tipos':tipos})

def productosmarca(request,marca):
    productos_mostrar=ProductoHasFotografia.objects.filter(producto_codigo_producto__marca_id_marca__pk=marca,fotografia_idfotografia__principal_fotografia=1,fotografia_idfotografia__estado_fotografia=1,producto_codigo_producto__estado_producto=1,producto_codigo_producto__publicar_producto=1,producto_codigo_producto__oferta_producto=0).annotate(total=Count('producto_codigo_producto')).values('producto_codigo_producto__pk','producto_codigo_producto__nombre_producto','producto_codigo_producto__descripcion_producto','fotografia_idfotografia__pk','fotografia_idfotografia__ruta_fotografia','producto_codigo_producto__marca_id_marca__nombre_marca').order_by('producto_codigo_producto__nombre_producto')
    marcas=Marca.objects.filter(estado_marca=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    generos=Genero.objects.filter(estado_genero=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    tipos=TipoProducto.objects.filter(estado_tipoproducto=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    return render(request,'kadoshapp/WEBproductos.html',{'productos':productos_mostrar,'marcas':marcas,'generos':generos,'tipos':tipos})

def productosgenero(request,genero):
    productos_mostrar=ProductoHasFotografia.objects.filter(producto_codigo_producto__genero_idgener__pk=genero,fotografia_idfotografia__principal_fotografia=1,fotografia_idfotografia__estado_fotografia=1,producto_codigo_producto__estado_producto=1,producto_codigo_producto__publicar_producto=1,producto_codigo_producto__oferta_producto=0).annotate(total=Count('producto_codigo_producto')).values('producto_codigo_producto__pk','producto_codigo_producto__nombre_producto','producto_codigo_producto__descripcion_producto','fotografia_idfotografia__pk','fotografia_idfotografia__ruta_fotografia','producto_codigo_producto__marca_id_marca__nombre_marca').order_by('producto_codigo_producto__nombre_producto')
    marcas=Marca.objects.filter(estado_marca=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    generos=Genero.objects.filter(estado_genero=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    tipos=TipoProducto.objects.filter(estado_tipoproducto=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    return render(request,'kadoshapp/WEBproductos.html',{'productos':productos_mostrar,'marcas':marcas,'generos':generos,'tipos':tipos})

def productostipo(request,tipo):
    productos_mostrar=ProductoHasFotografia.objects.filter(producto_codigo_producto__tipo_producto_idtipo_producto__pk=tipo,fotografia_idfotografia__principal_fotografia=1,fotografia_idfotografia__estado_fotografia=1,producto_codigo_producto__estado_producto=1,producto_codigo_producto__publicar_producto=1,producto_codigo_producto__oferta_producto=0).annotate(total=Count('producto_codigo_producto')).values('producto_codigo_producto__pk','producto_codigo_producto__nombre_producto','producto_codigo_producto__descripcion_producto','fotografia_idfotografia__pk','fotografia_idfotografia__ruta_fotografia','producto_codigo_producto__marca_id_marca__nombre_marca').order_by('producto_codigo_producto__nombre_producto')
    marcas=Marca.objects.filter(estado_marca=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    generos=Genero.objects.filter(estado_genero=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    tipos=TipoProducto.objects.filter(estado_tipoproducto=1,producto__publicar_producto=1,producto__estado_producto=1,producto__oferta_producto=0).distinct()
    return render(request,'kadoshapp/WEBproductos.html',{'productos':productos_mostrar,'marcas':marcas,'generos':generos,'tipos':tipos})

def detalleproductos(request,pk):
    producto=get_object_or_404(Producto,pk=pk)
    precio=Precio.objects.filter(producto_codigo_producto=producto,estado_precio=1).order_by('-pk')
    fotografias=ProductoHasFotografia.objects.filter(producto_codigo_producto__pk=pk,fotografia_idfotografia__estado_fotografia=1).values('fotografia_idfotografia__pk','fotografia_idfotografia__ruta_fotografia')
    return render(request,'kadoshapp/WEBdetalleproducto.html',{'producto':producto,'fotografias':fotografias,'precio':precio})
