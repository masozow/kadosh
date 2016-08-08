from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .formclientes import *

@login_required
def registro_cliente(request):
    if request.method == 'POST':
        form=Form_RegistroCliente_Persona(request.POST)
        if form.is_valid(): #validando a la persona
            ultima_persona=form.save()
            #return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
        else:
            print (f.errors)
            #mensaje error (raise error)
        sub_form=Form_RegistroCliente_Cliente(request.POST)
                #ultima_persona=Persona.objects.order_by('-idpersona')[:1]
                #[:1] es el equivalente de SQL a: TOP 1.
                #El - antes del nombre del campo indica que es en orden descendente
        if sub_form.is_valid():
            sf=sub_form.save(commit=False)
            #aqui solo se guarda el objeto del formulario del cliente en la variable sf
            #se le indica que no haga el commit para que aún no lo guarde en la BD
            sf.persona_idpersona=ultima_persona
            #se accede al campo persona_idpersona del modelo Cliente,
            #que se encuentra ya en el formulario, para cambiar su valor
            #por el que devuelve el queryset ultima_persona
            sf.save()
            #ahora sí se guarda
        else:
            print (sf.errors)
            #mensaje error (raise error)
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form=Form_RegistroCliente_Persona()
        sub_form=Form_RegistroCliente_Cliente()
    return render(request, 'kadoshapp/Datos_cliente.html', {'form': form, 'sub_form':sub_form})
