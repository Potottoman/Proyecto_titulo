from django.contrib import admin

from Almacen.models import Producto, Cliente, Proveedores, Deuda, Abono, ventas, OrdenPedido

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre", "categoria", "precio_venta", "stock")

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Proveedores)
admin.site.register(Deuda)
admin.site.register(Abono)
admin.site.register(ventas)
admin.site.register(OrdenPedido)
