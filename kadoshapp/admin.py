from django.contrib import admin
from .models import Color, Anaquel, CajaHasEmpleado, Caja

admin.site.register(Color)
admin.site.register(Anaquel)
admin.site.register(Caja)
admin.site.register(CajaHasEmpleado)
