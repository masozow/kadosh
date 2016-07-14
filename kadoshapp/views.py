from django.shortcuts import render
from .models import Persona, Cliente
from .forms import Form_RegistroClinte_Persona, Form_RegistroClinte_Cliente
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def ingreso_mercaderia(request):
    return render(request, 'kadoshapp/ingreso_mercaderia.html',{})


def registro(request):
    if request.method == 'POST':
        form=Form_RegistroClinte_Persona(request.POST)
        sub_form=Form_RegistroClinte_Cliente(request.POST)
        if form.is_valid() and sub_form.is_valid():
            form.save()
            sub_form.save()
            return render(request, 'kadoshapp/ingreso_mercaderi.html',{})

    else:
        form=Form_RegistroClinte_Persona()
        sub_form=Form_RegistroClinte_Cliente()
    return render(request, 'kadoshapp/Datos_cliente.html', {'form': form, 'sub_form':sub_form})
