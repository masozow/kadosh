from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Noticia(forms.ModelForm):
    class Meta:
        model=Noticia
        exclude=('estado_noticia',)

class Form_Fotografia(forms.ModelForm):
    class Meta:
        model=Fotografia
        fields=('ruta_fotografia',)
