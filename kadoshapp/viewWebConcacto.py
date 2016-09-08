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
from .formWebContacto import *
from django.db.models import Sum, Count
#from django.utils import timezone
#import datetime
#from datetime import datetime, timedelta
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
#from django.db.models import Q #para poder usar el operador | que funciona como OR
#from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)

from django.core.mail import send_mail #Falta configurar los settings


def contactanos(request):
    if request.method=='POST':
        form_contacto=Form_Contacto(request.POST) #se obtiene el formulario que vino con el request
        if form_contacto.is_valid(): #se comprueba que el formulario sea válido, es decir, que cumpla con las restricciones descritas en el model
            datos_contacto=form_contacto.cleaned_data
            #send_mail(datos_contacto['asunto_contacto'],'De:'datos_contacto['nombre_contacto']+'\n Mensaje: ' +datos_contacto['mensaje_contacto'], datos_contacto['correo_contacto'],['administradorkadosh@gmail.com'], fail_silently=False)
            guardar=form_contacto.save()
            form_contacto=Form_Contacto() #se obtiene un formulario limpio
    else:
        form_contacto=Form_Contacto() #se obtiene el formulario que vino con el request
    return render(request, 'kadoshapp/WEBcontacto.html', {'form_contacto':form_contacto})
