
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
import datetime

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
        form_busquedas=Form_Cliente_busquedas(request.POST)
        form_persona=Form_RegistroCliente_Persona(request.POST)
        form_cliente=Form_RegistroCliente_Cliente(request.POST)
        form=form_persona
        sub_form=form_cliente
        formbusqueda=form_busquedas
        persona=request.POST.get('id_persona')
        cliente=request.POST.get('id_cliente')
        nombres=request.POST.get('nombres_persona')
        apellidos=request.POST.get('apellidos_persona')
        dpi=request.POST.get('dpi_persona')
        direccion=request.POST.get('direccion_persona')
        telefonos=request.POST.get('telefonos_persona')
        fechanacimiento=datetime.date(int(request.POST.get('fecha_nacimiento_persona_year')),int(request.POST.get('fecha_nacimiento_persona_month')),int(request.POST.get('fecha_nacimiento_persona_day')))
        correo=request.POST.get('correoelectronico_persona')
        nit=request.POST.get('nit_cliente')
        tipo=request.POST.get('tipo_cliente_idtipo_cliente')
        res_persona=Persona.objects.filter(pk=int(persona)).update(nombres_persona=nombres,apellidos_persona=apellidos,dpi_persona=dpi,fecha_nacimiento_persona=fechanacimiento,correoelectronico_persona=correo,direccion_persona=direccion,telefonos_persona=telefonos)
        res_cliente=Cliente.objects.filter(pk=int(cliente)).update(nit_cliente=nit,tipo_cliente_idtipo_cliente=tipo)
        #if form_busquedas.is_valid():
        #    datos=form_busquedas.cleaned_data
        #    if form_persona.is_valid():
        #        persona=form_persona.cleaned_data
        #        if form_cliente.is_valid():
        #            cliente=form_cliente.cleaned_data
        #            res_persona=Persona.objects.filter(pk=int(datos['id_persona']))#.update(nombres_persona=persona['nombres_persona'],apellidos_persona=persona['apellidos_persona'],dpi_persona=persona['dpi_persona'],fecha_nacimiento_persona=datetime.date(datos['fecha_nacimiento_persona_year'],datos['fecha_nacimiento_persona_month'],datos['fecha_nacimiento_persona_day']),correoelectronico_persona=persona['correoelectronico_persona'],direccion_persona=persona['direccion_persona'],telefonos_persona=persona['telefonos_persona'])
        #            res_cliente=Cliente.object.filter(pk=int(datos['id_cliente']))#.update(nit_cliente=cliente['nit_cliente'],tipo_cliente_idtipo_cliente=cliente['tipo_cliente_idtipo_cliente'])
        #                #hasdf
        if res_persona and res_cliente:
            form=Form_RegistroCliente_Persona()
            sub_form=Form_RegistroCliente_Cliente()
            formbusqueda=Form_Cliente_busquedas()

        return render(request, 'kadoshapp/ModificarCliente.html', {'form': form, 'sub_form':sub_form,'formbusqueda':formbusqueda})
    else:
        form=Form_RegistroCliente_Persona()
        sub_form=Form_RegistroCliente_Cliente()
        formbusqueda=Form_Cliente_busquedas()
    return render(request, 'kadoshapp/ModificarCliente.html', {'form': form, 'sub_form':sub_form,'formbusqueda':formbusqueda})

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def BuscarCliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellido')
        nit = request.POST.get('nit')
        clientes=Cliente.objects.filter(persona_idpersona__nombres_persona__istartswith=nombre,persona_idpersona__apellidos_persona__istartswith=apellidos).values('pk','persona_idpersona__pk','persona_idpersona__nombres_persona','persona_idpersona__apellidos_persona','tipo_cliente_idtipo_cliente__nombre_tipocliente','fecha_registro_cliente','nit_cliente','persona_idpersona__dpi_persona','persona_idpersona__fecha_nacimiento_persona')
        if not apellidos and not nombre:
            clientes=Cliente.objects.filter(nit_cliente=nit).values('pk','persona_idpersona__pk','persona_idpersona__nombres_persona','persona_idpersona__apellidos_persona','tipo_cliente_idtipo_cliente__nombre_tipocliente','fecha_registro_cliente','nit_cliente','persona_idpersona__dpi_persona','persona_idpersona__fecha_nacimiento_persona')
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

@login_required
@user_passes_test(not_in_Caja_group, login_url='denegado')
def BuscarClienteEspecifico(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        persona = request.POST.get('persona')
        clientes=Cliente.objects.filter(persona_idpersona__pk=persona,pk=cliente).values('pk','persona_idpersona__pk','persona_idpersona__dpi_persona','persona_idpersona__nombres_persona','persona_idpersona__apellidos_persona','persona_idpersona__telefonos_persona','persona_idpersona__direccion_persona', 'persona_idpersona__fecha_nacimiento_persona','persona_idpersona__correoelectronico_persona','nit_cliente', 'tipo_cliente_idtipo_cliente__pk')
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
