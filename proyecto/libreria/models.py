from django.db import models
from datetime import date

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    paginas = models.IntegerField(default=100)
    portada = models.ImageField(upload_to='media/portadas/', null=True, blank=True)
    fecha_publicacion = models.DateField(default=date.today)
    descripcion = models.TextField()

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo
    
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    avatars = models.ImageField(upload_to='media/avatars/', null=True, blank=True)