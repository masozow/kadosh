from django.shortcuts import render
from .models import Persona, Cliente, TipoCliente
from .forms import Form_RegistroCliente_Persona, Form_RegistroCliente_Cliente
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
#importacion para form de IngresoMercaderiaPorProveedor
from .models import Producto, DetalleCompra, TipoProducto, Fotografia, InventarioProducto, Anaquel, Compra
from .forms import Form_IngresoMercaderiaPorProveedor_Producto, Form_IngresoMercaderiaPorProveedor_DetalleCompra, Form_IngresoMercaderiaPorProveedor_TipoProducto, Form_IngresoMercaderiaPorProveedor_Fotografia, Form_IngresoMercaderiaPorProveedor_InventarioProducto, Form_IngresoMercaderiaPorProveedor_Anaquel, Form_IngresoMercaderiaPorProveedor_Compra
#cosas de form Compra
from .models import Compra, InventarioProducto, Producto, DetalleCompra, Fotografia, Anaquel, TipoProducto
from .forms import Form_Compra_Compra, Form_Compra_InventarioProducto,Form_Compra_Producto, Form_Compra_DetalleCompra,Form_Compra_Fotografia, Form_Compra_Anaquel, Form_Compra_TipoProducto

# Create your views here.
def ingreso_mercaderia(request):
    return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
#Vista de form de compra
def Compra(request):
    if request.method=='POST':
        form_Compra=Form_Compra_Compra(request.POST)
        if form_Compra.is_valid():
            ultima_Compra=form_Compra.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Compra=Form_Compra_Compra()
        form_Detallecompra=Form_Compra_DetalleCompra()
        form_InventarioProducto=Form_Compra_InventarioProducto()
        form_Producto=Form_Compra_Producto()
        form_fotografia=Form_Compra_Fotografia()
        form_anaquel=Form_Compra_Anaquel()
        form_TipoProducto=Form_Compra_TipoProducto()
    return render(request, 'kadoshapp/Compra.html', {'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto, 'form_anaquel':form_anaquel, 'form_Compra':form_Compra })



#Vista de formulario de IngresoDeMercaderiaPorProveedor
def ingresodemercaderiaporProveedor(request):
    if request.method=='POST':
        form_Producto=Form_IngresoMercaderiaPorProveedor_Producto(request.POST)
        if form_Producto.is_valid():
            ultimo_producto=form_Producto.save()
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form_Producto=Form_IngresoMercaderiaPorProveedor_Producto()
        form_Detallecompra=Form_IngresoMercaderiaPorProveedor_DetalleCompra()
        form_TipoProducto=Form_IngresoMercaderiaPorProveedor_TipoProducto()
        form_fotografia=Form_IngresoMercaderiaPorProveedor_Fotografia()
        form_InventarioProducto=Form_IngresoMercaderiaPorProveedor_InventarioProducto()
        form_anaquel=Form_IngresoMercaderiaPorProveedor_Anaquel()
        form_Compra=Form_IngresoMercaderiaPorProveedor_Compra()
    return render(request, 'kadoshapp/IngresoMercaderiaPorProveedor.html', {'form_Producto': form_Producto,'form_Detallecompra':form_Detallecompra, 'form_TipoProducto':form_TipoProducto,'form_fotografia':form_fotografia ,'form_InventarioProducto':form_InventarioProducto, 'form_anaquel':form_anaquel, 'form_Compra':form_Compra })



def registro_cliente(request):
    if request.method == 'POST':
        form=Form_RegistroCliente_Persona(request.POST)
        if form.is_valid(): #validando a la persona
            ultima_persona=form.save()
            #return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
        else:
            print (f.errors)
            #mensaje error (raise error)
        sub_form=Form_RegistroCliente_Cliente(request.POST)
                #ultima_persona=Persona.objects.order_by('-idpersona')[:1]
                #[:1] es el equivalente de SQL a: TOP 1.
                #El - antes del nombre del campo indica que es en orden descendente
        if sub_form.is_valid():
            sf=sub_form.save(commit=False)
            #aqui solo se guarda el objeto del formulario del cliente en la variable sf
            #se le indica que no haga el commit para que aún no lo guarde en la BD
            sf.persona_idpersona=ultima_persona
            #se accede al campo persona_idpersona del modelo Cliente,
            #que se encuentra ya en el formulario, para cambiar su valor
            #por el que devuelve el queryset ultima_persona
            sf.save()
            #ahora sí se guarda
        else:
            print (sf.errors)
            #mensaje error (raise error)
        return render(request, 'kadoshapp/ingreso_mercaderia.html',{})
    else:
        form=Form_RegistroCliente_Persona()
        sub_form=Form_RegistroCliente_Cliente()
    return render(request, 'kadoshapp/Datos_cliente.html', {'form': form, 'sub_form':sub_form})
