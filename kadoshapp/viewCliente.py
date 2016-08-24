from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formclientes import *
def not_in_Caja_group(user):
    if user:
        return user.groups.filter(name='Caja').count() != 0
    return False

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def registro_cliente(request):
    if request.method == 'POST':
        form=Form_RegistroCliente_Persona(request.POST)
        sub_form=Form_RegistroCliente_Cliente(request.POST)
        if form.is_valid(): #validando a la persona
            if sub_form.is_valid():
                ultima_persona=form.save()
                sf=sub_form.save(commit=False)
                sf.persona_idpersona=ultima_persona
                sf.save()
                form=Form_RegistroCliente_Persona()
                sub_form=Form_RegistroCliente_Cliente()
            #ahora sí se guarda

            #mensaje error (raise error)
        return render(request, 'kadoshapp/Datos_cliente.html', {'form': form, 'sub_form':sub_form})
    else:
        form=Form_RegistroCliente_Persona()
        sub_form=Form_RegistroCliente_Cliente()
    return render(request, 'kadoshapp/Datos_cliente.html', {'form': form, 'sub_form':sub_form})
