from asyncio import sleep
import importlib
from multiprocessing import reduction
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Producto, Cliente
from django.contrib import messages



from Almacen.forms import AbonoForm, ClienteForm, DeudaForm, OrdenForm, ProveedorForm, ProductoForm

# Create your views here.


def index(request):
    return render(request, 'almacen/index.html')

def proveedor_view(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ProveedorForm()

    return render(request, 'almacen/general_form.html', {'form':form})

def producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ProductoForm()

    return render(request, 'almacen/general_form.html', {'form':form})    


def cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)             
        if form.is_valid():  
                       
            form.save()  
            messages.success(request, "Usuario agregado")
            return redirect('lista_cliente')
    else:
        form = ClienteForm()

    return render(request, 'almacen/general_form.html', {'form':form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    data = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_cliente')
        data["form"] = formulario
    
    return render(request, 'almacen/general_form.html', data)


def listar_cliente(request):
    listaCliente = Cliente.objects.all()

    data = {
        'clientes': listaCliente
    }

    return render(request, 'almacen/lista_cliente.html', data)

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    

    return redirect('lista_cliente')


def deuda_view(request):
    if request.method == 'POST':
        form = DeudaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = DeudaForm()

    return render(request, 'almacen/general_form.html', {'form':form})

def abono_view(request):
    if request.method == 'POST':
        form = AbonoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = AbonoForm()

    return render(request, 'almacen/general_form.html', {'form':form})

def orden_view(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = OrdenForm()

    return render(request, 'almacen/general_form.html', {'form':form})


def MostrarProd(request):
    productosListados =Producto.objects.all()

    return render(request, 'almacen/listado_prod.html', {'productos':productosListados})