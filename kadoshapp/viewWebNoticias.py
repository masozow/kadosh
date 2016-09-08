from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
#import json
#import pdb #para hacer el debugging
#from .models import Persona, Cliente, TipoCliente
#from .forms import Form_RegistroCliente_Persona, Form_RegistroCliente_Cliente
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
#from django_tables2 import RequestConfig
from .models import *
#from .tables import *
#from django.contrib.auth.decorators import login_required, user_passes_test
#from django.db.models import Sum, Count
#from django.utils import timezone
#import datetime
#from datetime import datetime, timedelta


# Creat your views here.
def noticias(request):
    noticias_mostrar=NoticiaHasFotografia.objects.filter(noticia_idnoticia__estado_noticia=1,vista_previa=1).values('noticia_idnoticia__pk','noticia_idnoticia__momento_publicacion_noticia','noticia_idnoticia__titulo_noticia','noticia_idnoticia__contenido_noticia','fotografia_idfotografia__ruta_fotografia').order_by('noticia_idnotica__momento_publicacion_noticia')
    return render(request,'kadoshapp/WEBnoticias.html',{'noticias':noticias_mostrar})


def detallenoticias(request,pk):
    noticia=Noticia.objects.filter(pk=pk)
    fotografias=NoticiaHasFotografia.objects.filter(noticia_idnoticia__pk=pk,fotografia_idfotografia__estado_fotografia=1).values('fotografia_idfotografia__pk','fotografia_idfotografia__ruta_fotografia')
    return render(request,'kadoshapp/WEBdetallenoticia.html',{'noticia':noticia,'fotografias':fotografias})


