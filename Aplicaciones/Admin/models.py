from django.db import models

# Modelo Cliente
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=10, unique=True, blank=True)
    nombres = models.CharField(max_length=75, blank=True)
    apellidos = models.CharField(max_length=75, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    foto = models.FileField(upload_to='fotoCliente' ,null=True, blank=True)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        fila = "{0}: {1} - {2} - {3} - {4} - {5} - {6}"
        return fila.format(self.id, self.ci, self.nombres, self.apellidos, self.direccion, self.telefono, self.email, self.foto, self.direccion)

# Modelo Categoria    
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.id, self.nombre, self.descripcion)

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, related_name="tipos", on_delete=models.CASCADE)
    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format( self.nombre, self.categoria.nombre)
                                 
# Modelo Producto
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='productos', default='')
    
    def __str__(self):
        fila = "{0}: {1} - {2} - {3} - {4} - {5} - {6}"
        return fila.format(self.id, self.nombre, self.precio, self.descripcion, self.imagen, self.categoria, self.tipo)