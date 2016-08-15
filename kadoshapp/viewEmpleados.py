from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .formEmpleados import *
from django.db.models import Q #para poder usar el operador | que funciona como OR
from django.db.models import F #para hacer llamadas u operaciones en la BD, sin cargarlas en memoria (no las procesa django, sino directamente el SGBD)
from collections import namedtuple #Sirve en la funcion de tuplas
from decimal import Decimal #para hacer la conversion decimal a JSON
import datetime #para hacer la conversion de fecha
from django.core.serializers.json import DjangoJSONEncoder

def not_in_Supervisor_group(user):
    if user:
        return user.groups.filter(name='Supervisor').count() != 0
    return False

@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def Empleados(request):
    if request.method=='POST':
        return render(request, 'kadoshapp/Empleados.html',{})
    else:
        form_empleado=Form_Empleados_Empleado()
        form_persona=Form_Empleados_Persona()
        form_puesto=Form_Empleados_Puesto()
        form_empleado.fields["puesto_idpuesto"].queryset = Puesto.objects.filter(estado_puesto=1)
        form_puesto.fields["puesto_idpuesto"].queryset = Puesto.objects.filter(estado_puesto=1)
    return render(request, 'kadoshapp/Empleados.html', {'form_puesto':form_puesto, 'form_persona':form_persona,  'form_empleado':form_empleado })


@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def BuscarEmpleados(request):
    if request.method == 'POST':
        rec_nombres = request.POST.get('nombres') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
        rec_apellidos = request.POST.get('apellidos')
        rec_puesto = request.POST.get('puesto')

        if not rec_puesto:
            rec_puesto=0

        response_data = {} #declarando un diccionario vacio
        lista_resultado=[]
        resp_consulta=consulta_sql_personalizada(rec_nombres,rec_apellidos,rec_puesto)

        for row in resp_consulta: #esto tal vez no sea necesario
            lista_resultado.append(row)

        return HttpResponse(
            json.dumps(lista_resultado,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



@login_required
@user_passes_test(not_in_Supervisor_group, login_url='denegado')
def CambiarPuestoEmpleado(request):
    if request.method == 'POST':
        rec_empleado = request.POST.get('empleado')
        rec_puesto = request.POST.get('puesto')

        Empleado.objects.filter(pk=rec_empleado).update(puesto_idpuesto=Puesto(pk=rec_puesto))

        response_data = {} #declarando un diccionario vacio
        response_data["respuesta"]="Empleado actualizado con éxito"

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def consulta_sql_personalizada(nombres,apellidos,puesto):
    from django.db import connection, transaction
    cursor = connection.cursor()

    cursor.execute("""select E.idEmpleado as id,CONCAT(Per.nombres_persona,' ',Per.apellidos_persona) as nombre,P.nombre_puesto as puesto,E.motivo_baja_empleado as motivo_baja,E.fecha_contratacion_empleado AS fecha_contratacion,E.fecha_baja_empleado as fecha_baja, SUM(V.total_venta) AS ventas_mes,E.fotografia_empleado as ruta_fotografia,E.Puesto_idPuesto as idp from Empleado as E
                      inner join Puesto as P on E.Puesto_idPuesto=P.idPuesto
                      inner join Venta as V on V.vendedor_venta=E.idEmpleado
                      inner join Persona as Per on E.Persona_idPersona=Per.idPersona
                      where (Per.nombres_persona like %s OR Per.apellidos_persona like %s OR E.Puesto_idPuesto=%s)
                      AND E.estado_empleado=1 AND V.estado_venta=1
                      AND
                      (YEAR(V.fecha_venta) = YEAR(Now())
                      AND MONTH(V.fecha_venta) = MONTH(Now()))""",[nombres,apellidos,puesto])
    row = dictfetchall(cursor)
    return row


#la siguiente funcion/metodo, sirve para devolver los datos en forma de diccionario
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

#la siguiente funcion devuelve los datos en forma de tupla con identificadores por nombre
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

#sobrecargando la funcion default de JSON, para poder enviar datos decimales
#def default(obj):
#    if isinstance(obj, Decimal):
#        return str(obj)
#    raise TypeError

#
#class DateTimeEncoder(json.JSONEncoder):
#    def default(self, obj):
#        if isinstance(obj, datetime.datetime):
#            return obj.isoformat()
#        elif isinstance(obj, datetime.date):
#            return obj.isoformat()
#        elif isinstance(obj, datetime.timedelta):
#            return (datetime.datetime.min + obj).time().isoformat()
#        else:
#            return super(DateTimeEncoder, self).default(obj)
