from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form para cierre de CierreDeCaja
class Form_RepDevolucion_Devolucion(forms.Form):
    fechainicial=forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    fechafinal=forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
