from cProfile import label
from dataclasses import fields
from django import forms

from Almacen.models import Proveedores, Producto, Cliente, Deuda, Abono, OrdenPedido

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedores

        fields = [
            'rut',
            'nombre',
            'apellido',
            'mail',
            'telefono',
            'rubro',
        ]
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'mail': 'Mail',
            'telefono': 'Telefono',
            'rubro': 'Rubro',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control'}) ,
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.TextInput(attrs={'class':'form-control'}),

        }

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'codigo_barra',
            'nombre',
            'categoria',
            'descripcion',
            'precio_compra',
            'precio_venta',
            'stock',
        ]
        labels = {
            'codigo_barra': 'Codigo de barra',
            'nombre': 'Nombre',
            'categoria': 'Categoria',
            'descripcion': 'Descripcion',
            'precio_compra': 'Precio de compra',
            'precio_venta': 'Precio de venta',
            'stock': 'Stock',
        }
        widgets = {
            'codigo_barra': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'precio_compra': forms.TextInput(attrs={'class':'form-control'}),
            'precio_venta': forms.TextInput(attrs={'class':'form-control'}),
            'stock': forms.TextInput(attrs={'class':'form-control'}),

        }

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [
            'rut',
            'nombre',
            'apellido',
            'mail',
        ]
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'mail': 'Mail',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control'}) ,
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.TextInput(attrs={'class':'form-control'}),
        }

class DeudaForm(forms.ModelForm):

    class Meta:
        model = Deuda   

        fields = [
            'deudor',
            'deuda',
            'cant_pagado',
            'estado',
        ]
        labels = {
            'deudor': 'Deudor',
            'deuda': 'Cantidad deuda',
            'cant_pagado': 'Cantidad abonada',
            'estado': 'Pagado',
        }
        widgets = {
            'deudor': forms.Select(attrs={'class':'form-control'}),
            'deuda': forms.TextInput(attrs={'class':'form-control'}),
            'cant_pagado': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput,

        }


class AbonoForm(forms.ModelForm):

    class Meta:
        model = Abono

        fields = [
            'deudor',
            'monto',
        ]
        labels = {
            'deudor': 'Deudor',
            'monto': 'Monto a abonar',
        }
        widgets = {
            'deudor': forms.Select(attrs={'class':'form-control'}),
            'monto': forms.TextInput(attrs={'class':'form-control'}),
        }

class OrdenForm(forms.ModelForm):

    class Meta:
        model = OrdenPedido

        fields = [
            'proveedor',
            'nombreProd',
            'cantidad',
        ]
        labels = {
            'proveedor': 'Proveedor',
            'nombreProd': 'Nombre Producto',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'proveedor': forms.Select(attrs={'class':'form-control'}),
            'nombreProd': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
        }
