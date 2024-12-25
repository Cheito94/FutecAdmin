from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.inicio, name='inicio'),

    #----------CLIENTE----------
    path('listarClientes/', views.listarClientes, name='listarClientes'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
    path('editarCliente/<id>/', views.editarCliente, name='editarCliente'),
    path('eliminarCliente/<int:id>/', views.eliminarCliente, name='eliminarCliente'),    
    
    #----------CATEGORIA----------
    path('listarCategorias/', views.listarCategorias, name='listarCategorias'),
    path('crearCategoria/', views.crearCategoria, name='crearCategoria'),
    path('editarCategoria/<id>/', views.editarCategoria, name='editarCategoria'),
    path('eliminarCategoria/<int:id>/', views.eliminarCategoria, name='eliminarCategoria'),

    #----------PRODUCTO----------
    path('listarProductos/', views.listarProductos, name='listarProductos'),
    path('crearProducto/', views.crearProducto, name='crearProducto'),
    path('editarProducto/<id>/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:id>/', views.eliminarProducto, name='eliminarProducto'),
    # Otras rutas
    path('obtenerTipos/<int:categoria_id>/', views.obtener_tipos, name='obtener_tipos'),
    
]


