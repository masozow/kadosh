from django import forms
from .models import Persona,Cliente,TipoCliente
from django.forms import ModelChoiceField,Select
from django.contrib.admin import widgets

#form Cliente
class Form_RegistroCliente_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        exclude=('estado_persona',)
        #fields=('dpi_persona','nombres_persona','apellidos_persona','telefonos_persona','direccion_persona','fecha_nacimiento_persona',)
        widgets = {
            'fecha_nacimiento_persona': widgets.AdminDateWidget(),
            #forms.DateInput(format='%d/%m/%Y'),
            #DateInput(attrs={'class':'datepicker'}), #Esto es para usar jquery
        }


class Form_RegistroCliente_Cliente(forms.ModelForm):
    class Meta:
        #opciones=TipoCliente.objects.filter(estado_tipocliente=1)
        model=Cliente
        exclude=('persona_idpersona','estado_cliente','fecha_registro_cliente',)
        #Personalizando las caracteristicas de los campos
        #widgets = {#widgets se utiliza para colocar ciertos controles html en lugar de textbox,
                    #como campos de fecha, radiobutton, checkbox, DropDownList(select en html), etc
                    #en este caso se utiliza un Select que sirve como DropDownList
                    #el atributo 'to_field_name' sirve como el 'combobox.value' de C#
            #'tipo_cliente_idtipo_cliente': Select( (x.idtipo_cliente, x.nombre_tipocliente) for x in opciones ),
            #Lo siguiente no funcionó
            #ModelChoiceField(queryset=TipoCliente.objects.filter(estado_tipocliente=1),to_field_name='idtipo_cliente'),#forms.ChoiceField(),
        #}
        #labels = { #Cambia las etiquetas por defecto para cada campo
        #    'tipo_cliente_idtipo_cliente': ('Tipo cliente: '),
        #}
        #help_texts = { #Muestra un texto de ayuda para el campo
        #    'tipo_cliente_idtipo_cliente': ('Elija el tipo de cliente, puede ser Mayorista, Normal, etc.'),
        #}
        #error_messages = { #Mensajes de error dependiendo de la condicion indicada
        #    'name': {
        #        'max_length': _("This writer's name is too long."),
        #    },
        #}
