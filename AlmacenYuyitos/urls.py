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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from Almacen import views 
from django.contrib.auth.views import logout_then_login,LoginView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(views.index), name = 'index'),
    path('addprov/', login_required(views.proveedor_view) , name = 'add_proveedor'),
    path('addprod/', login_required(views.producto_view) , name = 'add_producto'),
    path('addcliente/', login_required(views.cliente_view), name = 'add_cliente'),
    path('adddeuda/', login_required(views.deuda_view) , name = 'add_deuda'),
    path('addabono/', login_required(views.abono_view) , name = 'add_abono'),
    path('addorden/', login_required(views.orden_view) , name = 'add_orden'),
    path('listaProd/', login_required(views.MostrarProd) , name = 'Mostrar_prod'),
    path('listaCli/', login_required(views.listar_cliente) , name = 'lista_cliente'),
    path('eliminarCliente/<id>', login_required(views.eliminar_cliente) , name = 'eliminar_cliente'),
    path('editarCliente/<id>', login_required(views.editar_cliente) , name = 'editar_cliente'),
    path('accounts/login/', LoginView.as_view(template_name='almacen/login.html'), name = 'login'),
    path('logout/', logout_then_login, name = 'logout'),
]
