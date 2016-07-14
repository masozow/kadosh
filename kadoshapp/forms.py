from django import forms
from .models import Persona,Cliente

#form Cliente
class Form_RegistroClinte_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        fields=('dpi_persona','nombres_persona','apellidos_persona','telefonos_persona','direccion_persona','fecha_nacimiento_persona',)

class Form_RegistroClinte_Cliente(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=('nit_cliente','tipo_cliente_idtipo_cliente',)

    #def __str__(self):
    #    return 'Nit: %s - Nombre: %s %s' % (self.nit_cliente, self.persona_idpersona.nombres_persona, self.persona_idpersona.apellidos_persona)
