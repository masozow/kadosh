from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from .models import *
from .formPublicarNoticia_Web import *



def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def not_in_Web_group(user):
    if user:
        return user.groups.filter(name='Web').count() != 0
    return False

@login_required
@user_passes_test(not_in_Web_group, login_url='denegado')
def noticia(request):
    if request.method=='POST':
        form_noticia=Form_Noticia(request.POST)
        form_fotografia=Form_Fotografia(request.POST, request.FILES)
        if form_noticia.is_valid():
            if form_fotografia.is_valid():
                foto=form_fotografia.save(commit=False)
                foto.principal_fotografia=1
                foto.estado_fotografia=1
                foto.save()
                noticia=form_noticia.save()
                noticiahasfotografia=NoticiaHasFotografia(noticia_idnoticia=noticia,fotografia_idfotografia=foto,vista_previa=1)
                noticiahasfotografia.save()
                form_noticia=Form_Noticia()
                form_fotografia=Form_Fotografia()
    else:
        form_noticia=Form_Noticia()
        form_fotografia=Form_Fotografia()
    return render(request, 'kadoshapp/PublicarNoticia_Web.html', {'form_noticia':form_noticia, 'form_fotografia':form_fotografia })