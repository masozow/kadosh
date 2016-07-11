from django.shortcuts import render

# Create your views here.
def ingreso_mercaderia(request):
    return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
