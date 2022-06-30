"""AlmacenYuyitos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Almacen import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('addprov/', views.proveedor_view , name='add_proveedor'),
    path('addprod/', views.producto_view , name='add_producto'),
    path('addcliente/', views.cliente_view, name='add_cliente'),
    path('adddeuda/', views.deuda_view , name='add_deuda'),
    path('addabono/', views.abono_view , name='add_abono'),
    path('addorden/', views.orden_view , name='add_orden'),
    path('listaProd/', views.MostrarProd , name='Mostrar_prod'),
    path('listaCli/', views.listar_cliente , name='lista_cliente'),
    path('listaProv/', views.listar_proveedor , name='lista_proveedor'),
    path('eliminarCliente/<id>', views.eliminar_cliente , name='eliminar_cliente'),
    path('editarCliente/<id>', views.editar_cliente , name='editar_cliente'),
    path('editarProveedor/<id>', views.editar_Proovedor , name='editar_proveedor'),
    path('eliminarProveedor/<id>', views.eliminar_proovedor, name='eliminar_proveedor'),
    path('agregaProducto/<id>', views.agregar_producto , name='agregar_prod'),
    path('eliminarProducto/<id>', views.eliminar_producto , name='eliminar_prod'),
    path('restarProducto/<id>', views.restar_producto , name='restar_prod'),
    path('limpiarProducto/', views.limpiar_carrito , name='limpiar_prod'),
    path('comprar/', views.comprar , name='comprar'),
]
