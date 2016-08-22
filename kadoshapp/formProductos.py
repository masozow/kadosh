from django import forms
from django.forms import widgets
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Producto_Color(forms.ModelForm):
    class Meta:
        model=Color
        fields=('nombre_color',)

class Form_Producto_Estilo(forms.ModelForm):
    class Meta:
        model=Estilo
        fields=('nombre_estilo',)

class Form_Producto_Genero(forms.ModelForm):
    class Meta:
        model=Genero
        fields=('nombre_genero',)

class Form_Producto_Marca(forms.ModelForm):
    class Meta:
        model=Marca
        fields=('nombre_marca',)

class Form_Producto_Talla(forms.ModelForm):
    class Meta:
        model=Talla
        fields=('nombre_talla',)

class Form_Producto_Tipo(forms.ModelForm):
    class Meta:
        model=TipoProducto
        fields=('nombre_tipoproducto',)
