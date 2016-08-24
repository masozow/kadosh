from django import forms
from .models import Persona,Empleado
from django.contrib.admin import widgets
from django.forms import extras
#form Cliente
class Form_RegistroEmpleado_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        exclude=('estado_persona',)
        widgets = {
            'fecha_nacimiento_persona': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class Form_RegistroEmpleado_Empleado(forms.ModelForm):
    def __init__(self, *args, **kwargs):  #este codigo hace que el codigo de producto no sea necesario, así no se tiene un error de validación al no enviarlo
        # first call parent's constructor
        super(Form_RegistroEmpleado_Empleado, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['auth_user'].required = False
    class Meta:
        model=Empleado
        exclude=('persona_idpersona','estado_empleado',)
        widgets = {
            'fecha_contratacion_empleado': forms.DateInput(attrs={'class': 'datepicker'}),

        }

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
