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
def inicio(request):
    infoindex=Index.objects.filter(pk=1)
    fotosindex=IndexHasFotografia.objects.filter(index_idindex=infoindex).values('fotografia_idfotografia__pk','fotografia_idfotografia__ruta_fotografia','ubicacion_fotografiaindex')
    return render(request,'kadoshapp/WEBindex.html',{'infoindex':infoindex,'fotosindex':fotosindex})
    #{% fotosindex.fotografia_idfotografia__ruta_fotografia %}