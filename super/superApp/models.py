from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(default="",max_length=50)
    categoria = models.CharField(default="",max_length=50)
    stock = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='images/', null=False, blank=False)
    

class Formulario(models.Model):
    tipo_consulta = models.CharField(default="",max_length=100)
    correo_electronico = models.EmailField(default="",max_length=100)
    imagen = models.ImageField(upload_to="images/", blank=False, null=False)
    telefono = models.IntegerField(default=0)
    descripcion = models.CharField(default="",max_length=500)
    estado = models.CharField(default="Pendiente",max_length=100)