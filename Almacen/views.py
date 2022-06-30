from asyncio import sleep
import imp
import importlib
from multiprocessing import reduction
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from Almacen.Carrito import Carrito
from .models import Producto, Cliente, Proveedores
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
            messages.success(request, 'Proveedor agregado correctamente.')
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

def listar_proveedor(request):
    listaProveedores = Proveedores.objects.all()

    data = {
        'proveedores': listaProveedores
    }

    return render(request, 'almacen/lista_proveedor.html', data)

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, "Cliente Eliminado")
    return redirect('lista_cliente')

def eliminar_proovedor(request, id):
    proveedor = get_object_or_404(Proveedores, id=id)
    proveedor.delete()
    messages.success(request, "Proveedor Eliminado")
    return redirect('lista_proveedor')

def Proveedor_view(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)             
        if form.is_valid():                         
            form.save()  
            messages.success(request, "Proveedor agregado correctamente.")
            return redirect('lista_proveedor')
    else:
        form = ProveedorForm()

    return render(request, 'almacen/general_form.html', {'form':form})

def editar_Proovedor(request, id):
    proveedor = get_object_or_404(Proveedores, id=id)

    data = {
        'form': ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor editado correctamente.")
            return redirect('lista_proveedor')
        data["form"] = formulario
    
    return render(request, 'almacen/general_form.html', data)




def deuda_view(request):
    if request.method == 'POST':
        form = DeudaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Deuda ingresada")
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
    # trae el objeto de producto
    producto1 = Producto.objects.filter(id=id)
    # se obtiene el valor del stock
    stock = producto1.values()[0]["stock"]
    # por cada click en el botón se le resta 1 al stock total
    total = int(stock) - 1
    # se le pasa el stock restado al producto
    producto.stock = total
    # se guarda en la bbdd
    producto.save()
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

def comprar(request):
    carrito = Carrito(request)
    carrito.limpiar()
    messages.success(request, "Productos comprados correctamente.")
    return redirect("Mostrar_prod")
