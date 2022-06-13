from multiprocessing import reduction
from django.shortcuts import redirect, render
from django.http import HttpResponse

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
        return redirect('index')
    else:
        form = ClienteForm()

    return render(request, 'almacen/general_form.html', {'form':form})

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