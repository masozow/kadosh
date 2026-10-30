"""
Crea un usuario administrador de demo y los grupos que exige la aplicación.

Las vistas de Kadosh solo dejan entrar a usuarios que pertenezcan a ciertos
grupos (ni siquiera un superusuario pasa sin ellos), por eso este script
crea los 6 grupos y mete al usuario en todos.

Uso:  python crear_demo.py [usuario] [contraseña]
"""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemakadosh.settings_demo')

import django
django.setup()

from django.contrib.auth.models import Group, User

GRUPOS = ['Caja', 'Bodega', 'AdministradorSistema', 'Supervisor', 'Web', 'Traslado']

usuario = sys.argv[1] if len(sys.argv) > 1 else 'admin'
clave = sys.argv[2] if len(sys.argv) > 2 else 'admin1234'

user, creado = User.objects.get_or_create(
    username=usuario,
    defaults={'is_staff': True, 'is_superuser': True, 'email': usuario + '@example.com'},
)
if creado:
    user.set_password(clave)
    user.save()

for nombre in GRUPOS:
    grupo, _ = Group.objects.get_or_create(name=nombre)
    user.groups.add(grupo)

print('Usuario: %s (%s)' % (usuario, 'creado, clave: ' + clave if creado else 'ya existía, clave sin cambios'))
print('Grupos asignados: ' + ', '.join(GRUPOS))
