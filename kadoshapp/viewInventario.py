from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import pdb #para hacer el debugging
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import *
from .formInventario import *
#vista Inventario
@login_required
def Inventario(request):
    if request.method=='POST':
        form_inventario=Form_Inventario_InventarioProducto(request.POST)
        if form_inventario.is_valid():
            ultimo_inventario=form_inventario.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_inventario=Form_Inventario_InventarioProducto()
        #form_anaquel=Form_Inventario_Anque()
        #form_detallainventario=Form_Inventario_DetalleInventarioRealizado()
        form_empleado=Form_Inventario_Empleado()
        form_ajusteinventario=Form_Inventario_AjusteInventario()
        #form_inventariorealizado=Form_Inventario_InventarioRealizado();
    return render(request, 'kadoshapp/Inventario.html', {'form_inventario':form_inventario, 'form_empleado':form_empleado , 'form_ajusteinventario':form_ajusteinventario  })
