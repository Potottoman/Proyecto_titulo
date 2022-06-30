from asyncio import sleep
import imp
import importlib
from multiprocessing import reduction
import re
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views import View

from Almacen.Carrito import Carrito
from Almacen.context_processor import total_pagar
from Almacen.utils import render_to_pdf
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
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('Mostrar_prod')
    else:
        form = ProductoForm()

    return render(request, 'almacen/general_form.html', {'form':form})    

def listar_productos(request):
    listaProductos = Producto.objects.all()

    data = {
        'productos': listaProductos
    }

    return render(request, 'almacen/lista_prod.html', data)


def cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)             

        if form.is_valid():                         

            form.save()  
            messages.success(request, "Cliente agregado correctamente.")
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
            messages.success(request, "Cliente editado correctamente.")
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
    messages.success(request, "Cliente Eliminado")
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


def agregar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.agregar(producto)
    return redirect("Mostrar_prod")

def eliminar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.eliminar(producto)
    return redirect("Mostrar_prod")

def restar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.restar(producto)
    return redirect("Mostrar_prod")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Mostrar_prod")

class FacturaPdf(View):
    def get(self, request, *args, **kwargs):
        total = 0
    # if request.user.is_authenticated:
        # if "carrito" in request.session.keys():
            
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])   
            carrito = request.session["carrito"].items()
            data = {
                'carrito' : carrito,
                'total_carrito' : total
            }
            pdf = render_to_pdf('Almacen/factura.html', data)
            carritos = Carrito(request)
            carritos.limpiar()
            return HttpResponse(pdf,content_type='application/pdf')
        else:
            return None
