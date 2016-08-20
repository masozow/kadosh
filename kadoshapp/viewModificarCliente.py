from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formModificarCliente import *
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def not_in_Caja_group(user):
    if user:
        return user.groups.filter(name='Caja').count() != 0
    return False

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def mod_cliente(request):
    if request.method == 'POST':
        form=Form_RegistroCliente_Persona(request.POST)
        #if form.is_valid(): #validando a la persona
        #else:
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form=Form_RegistroCliente_Persona()
        sub_form=Form_RegistroCliente_Cliente()
        formbusqueda=Form_Cliente_busquedas()
    return render(request, 'kadoshapp/ModificarCliente.html', {'form': form, 'sub_form':sub_form,'formbusqueda':formbusqueda})


def BuscarCliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        nit = request.POST.get('nit')
        if not nombre:
            nombre=''
        if not apellidos:
            apellidos=''
        if not nit:
            nit=''
        clientes = clientes=Cliente.objects.filter(persona_idpersona__nombres_persona__startswith=nombre,persona_idpersona__apellidos_persona__startswith=apellidos,nit_cliente=nit).values('pk','persona_idpersona__pk','persona_idpersona__nombres_persona','persona_idpersona__apellidos_persona','tipo_cliente_idtipo_cliente__nombre_tipocliente','fecha_registro_cliente')
        if not clientes:
            clientes=Cliente.objects.filter(persona_idpersona__nombres_persona__startswith=nombre,persona_idpersona__apellidos_persona__startswith=apellidos).values('pk','persona_idpersona__pk','persona_idpersona__nombres_persona','persona_idpersona__apellidos_persona','tipo_cliente_idtipo_cliente__nombre_tipocliente','fecha_registro_cliente')
            if not clientes:
                clientes=Cliente.objects.filter(nit_cliente=nit).values('pk','persona_idpersona__pk','persona_idpersona__nombres_persona','persona_idpersona__apellidos_persona','tipo_cliente_idtipo_cliente__nombre_tipocliente','fecha_registro_cliente')
        cliente_diccionario=ValuesQuerySetToDict(clientes)
        return HttpResponse(
            json.dumps(cliente_diccionario,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
