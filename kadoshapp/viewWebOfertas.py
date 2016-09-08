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
def ofertas(request):
    productos_mostrar=ProductoHasFotografia.objects.filter(fotografia__principal_fotografia=1,fotografia__estado_fotografia=1,producto__estado_producto=1,producto__publicar_producto=1,producto__oferta_producto=1).values('producto__pk','producto__marca_idmarca__nombre_marca','producto__nombre_producto','producto__descripcion_producto','producto__tipo_producto_idtipo_producto__nombre_tipoproducto','producto__color_idcolor__nombre_color','producto__talla_idtalla__nombre_talla','producto__estilo_idestilo__nombre_estilo','producto__genero_idgener__nombre_genero','fotografia__pk','fotografia__ruta_fotografia').order_by('producto__marca_idmarca__nombre__marca','producto__talla_idtalla__nombre_talla')
    return render(request,'kadoshapp/ingreso_mercaderia.html',{'productos':productos_mostrar})


def detalleofertas(request,pk):
    producto=Producto.objects.filter(pk=pk)
    fotografias=ProductoHasFotografia.objects.filter(producto__pk=pk,fotografia__estado_fotografia=1).values('fotografia__pk','fotografia__ruta_fotografia')
    return render(request,'kadoshapp/ingreso_mercaderia.html',{'producto':producto,'fotografias':fotografias})

def avanzar_retroceder_productos(request):
    if request.method == 'POST':
        inicio = int(request.POST.get('inicio'))
        final = int(request.POST.get('final'))
        todosproductos=ProductoHasFotografia.objects.filter(fotografia__principal_fotografia=1,fotografia__estado_fotografia=1,producto__estado_producto=1,producto__publicar_producto=1,producto__oferta_producto=1).values('producto__pk','producto__marca_idmarca__nombre_marca','producto__nombre_producto','producto__descripcion_producto','producto__tipo_producto_idtipo_producto__nombre_tipoproducto','producto__color_idcolor__nombre_color','producto__talla_idtalla__nombre_talla','producto__estilo_idestilo__nombre_estilo','producto__genero_idgener__nombre_genero','fotografia__pk','fotografia__ruta_fotografia').order_by('producto__marca_idmarca__nombre__marca','producto__talla_idtalla__nombre_talla').annotate(total=count('pk'))
        
        if inicio<0: #tope menor del inicio
        	inicio=0
        if final<20: #tope menor del final
        	final=20
        if inicio==final: #tope mayor del inicio
            inicio=final-1
        if final>=int(todosproductos.total): #tope mayor del final
        	final=int(todosproductos.total)
        
        #probar esto para avanzar o retroceder productos
        productos=ProductoHasFotografia.objects.filter(fotografia__principal_fotografia=1,fotografia__estado_fotografia=1,producto__estado_producto=1,producto__publicar_producto=1,producto__oferta_producto=0).values('producto__pk','producto__marca_idmarca__nombre_marca','producto__nombre_producto','producto__descripcion_producto','producto__tipo_producto_idtipo_producto__nombre_tipoproducto','producto__color_idcolor__nombre_color','producto__talla_idtalla__nombre_talla','producto__estilo_idestilo__nombre_estilo','producto__genero_idgener__nombre_genero','fotografia__pk','fotografia__ruta_fotografia').order_by('producto__marca_idmarca__nombre__marca','producto__talla_idtalla__nombre_talla')[inicio:final]
        dict_producto=ValuesQuerySetToDict(productos)
        return HttpResponse(
            json.dumps(dict_producto,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )