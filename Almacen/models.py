from functools import total_ordering
from venv import create
from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo_barra=models.IntegerField()
    nombre=models.CharField(max_length=30)
    categoria=models.CharField(max_length=32)
    descripcion=models.CharField(max_length=50)
    precio_compra=models.IntegerField()
    precio_venta=models.IntegerField()
    stock=models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    mail=models.EmailField()

    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    mail=models.EmailField()
    telefono=models.CharField(max_length=10)
    rubro=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Deuda(models.Model):
    deudor=models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    deuda=models.IntegerField()
    cant_pagado=models.IntegerField()
    estado=models.BooleanField()

    def __int__(self):
        return self.deudor

class Abono(models.Model):
    deudor=models.ForeignKey(Deuda, null=True, blank=True, on_delete=models.CASCADE)
    monto=models.IntegerField()

    def __int__(self):
        return self.deudor

class ventas(models.Model):
    productos=models.CharField(max_length=20)
    fecha=models.DateField()
    total=models.IntegerField()

class OrdenPedido(models.Model):
    proveedor= models.ForeignKey(Proveedores, null=True, blank=True, on_delete=models.CASCADE)
    nombreProd=models.CharField(max_length=20)
    cantidad=models.IntegerField()

    def __str__(self):
        return self.proveedor


