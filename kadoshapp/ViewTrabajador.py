from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formTrabajador import *
from django.contrib.auth import login

def not_in_Supervisor_group(user):
    if user:
        return user.groups.filter(name='Supervisor').count() != 0
    return False

@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def registro_trabajador(request):
    if request.method == 'POST':
        form=Form_RegistroEmpleado_Persona(request.POST)
        form_usuario=UserForm(request.POST)
        sub_form=Form_RegistroEmpleado_Empleado(request.POST, request.FILES)
        if form.is_valid(): #validando a la persona
            if form_usuario.is_valid():
                if sub_form.is_valid():
                    try:
                        ultima_persona=form.save()
                        new_user = User.objects.create_user(**form_usuario.cleaned_data)
                        #ultimo_usuario=new_user.save()
                        sf=sub_form.save(commit=False)
                        sf.persona_idpersona=ultima_persona
                        sf.auth_user=new_user
                        sf.save()
                        form=Form_RegistroEmpleado_Persona()
                        form_usuario=UserForm()
                        sub_form=Form_RegistroEmpleado_Empleado()
                    except Exception as e:
                        errores=str(e)
            #mensaje error (raise error)
        return render(request, 'kadoshapp/Trabajador.html', {'form': form, 'sub_form':sub_form,'form_usuario':form_usuario})
    else:
        form=Form_RegistroEmpleado_Persona()
        sub_form=Form_RegistroEmpleado_Empleado()
        form_usuario=UserForm()
    return render(request, 'kadoshapp/Trabajador.html', {'form': form, 'sub_form':sub_form,'form_usuario':form_usuario})
