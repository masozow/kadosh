from django import forms
from django.forms import widgets
#from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Contacto(forms.ModelForm):
    class Meta:
        model=Contacto
        exclude=('estado_contacto','fecha_contacto')
        widgets = {
            'correo_contacto': forms.EmailInput(attrs={'class': 'validate'}),
            'mensaje_contacto': forms.Textarea()
        }
        