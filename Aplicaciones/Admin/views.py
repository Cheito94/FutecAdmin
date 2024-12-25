from typing import  Counter
from django.shortcuts import render
from . models import Cliente, Categoria, Tipo, Producto
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

#----------CLIENTE----------
def listarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listarClientes.html', {'clientes': clientes})

def crearCliente(request):
    if request.method == 'POST':
        ced = request.POST['ci']
        nomb = request.POST['nombres']
        apell = request.POST['apellidos']
        dir = request.POST['direccion']
        tel = request.POST['telefono']
        correo = request.POST['email']
        fot = request.FILES.get('foto')
        desc = request.POST['descripcion']
        if Cliente.objects.filter(ci=ced).exists():
            messages.error(request, 'Ya existe un cliente con esta cédula.')
            return render(request, 'crearCliente.html')
        nuevoCliente = Cliente.objects.create(ci=ced, nombres=nomb, apellidos=apell, direccion=dir, telefono= tel, email=correo, foto=fot, descripcion=desc)
        messages.success(request, 'Cliente guardado con éxito')
        return redirect('listarClientes')
    clientes = Cliente.objects.all()
    return render(request, 'crearCliente.html', {'clientes': clientes})

def editarCliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.ci = request.POST['ci']
        cliente.nombres = request.POST['nombres']
        cliente.apellidos = request.POST['apellidos']
        cliente.direccion = request.POST['direccion']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.foto = request.FILES.get('foto')
        cliente.descripcion = request.POST['descripcion']
        cliente.save()
        messages.success(request, 'Cliente actualizado con éxito')
        return redirect('listarClientes')
    
def eliminarCliente(request, id):
    clienteEliminar = get_object_or_404(Cliente, id=id)
    clienteEliminar.delete()
    messages.success(request, 'Cliente eliminado con éxito')
    return redirect('listarClientes')

#----------CATEGORIA----------
def listarCategorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'listarCategorias.html', {'categorias': categorias})

def crearCategoria(request):
    if request.method == 'POST':
        nomb = request.POST.get('nombre')
        desc = request.POST.get('descripcion')
        tipos = request.POST.getlist('tipos[]')
        if Categoria.objects.filter(nombre=nomb).exists():
            messages.error(request, 'Ya existe una categoría con este nombre.')
            return render(request, 'crearCategoria.html')
        nuevaCategoria = Categoria.objects.create(nombre=nomb, descripcion=desc)
        for tipo_nombre in tipos:
            if tipo_nombre.strip():
                Tipo.objects.create(nombre=tipo_nombre, categoria=nuevaCategoria)
        messages.success(request, 'Categoría y tipos creados con éxito')
        return redirect('listarCategorias')
    return render(request, 'crearCategoria.html')

def obtener_tipos(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    tipos = Tipo.objects.filter(categoria=categoria)
    tipos_data = [{'id': tipo.id, 'nombre': tipo.nombre} for tipo in tipos]
    return JsonResponse({'tipos': tipos_data})

def editarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.descripcion = request.POST['descripcion']
        categoria.save()
        messages.success(request, 'Categoría actualizada con éxito')
        return redirect('listarCategorias')

def eliminarCategoria(request, id):
    categoriaEliminar = get_object_or_404(Categoria, id=id)
    categoriaEliminar.delete()
    messages.success(request, 'Categoría eliminada con éxito')
    return redirect('listarCategorias')

#----------PRODUCTO----------
def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'listarProductos.html', {'productos': productos})

def crearProducto(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        nomb = request.POST['nombre']
        prec = request.POST['precio']
        desc = request.POST['descripcion']
        img = request.FILES.get('imagen')  # Si tienes un campo de imagen
        categoria_id = request.POST['categoria']
        tipo_id = request.POST['tipo']
        # Obtener la categoría y tipo seleccionados
        categoria = Categoria.objects.get(id=categoria_id)
        tipo = Tipo.objects.get(id=tipo_id)
        # Crear el producto
        producto = Producto(nombre=nomb, precio=prec, descripcion=desc, imagen=img, categoria=categoria, tipo=tipo)
        producto.save()
        # Redirigir a la lista de productos después de crear uno
        return redirect('listarProductos')  
    else:
        # Obtener todas las categorías
        categorias = Categoria.objects.all()
        # Pasar las categorías al contexto
        context = {
            'categorias': categorias,
        }
        return render(request, 'crearProducto.html', context)

def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.descripcion = request.POST['descripcion']
        
        # Si se sube una nueva imagen, la asignamos
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        
        # Asignar categoría y tipo
        categoria = Categoria.objects.get(id=request.POST['categoria'])
        tipo = Tipo.objects.get(id=request.POST['tipo'])
        producto.categoria = categoria
        producto.tipo = tipo
        producto.save()
        messages.success(request, 'Producto actualizado con éxito')
        return redirect('listarProductos')
    return render(request, 'editarProducto.html', {
        'producto': producto,
        'categorias': categorias
    })
    
def eliminarProducto(request, id):
    productoEliminar = get_object_or_404(Producto, id=id)
    productoEliminar.delete()
    messages.success(request, 'Producto eliminado con éxito')
    return redirect('listarProductos')

        

