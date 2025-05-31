from django.db import models
from datetime import date

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    paginas = models.IntegerField(default=100)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    fecha_publicacion = models.DateField(default=date.today)
    descripcion = models.TextField()

    precio = models.DecimalField(max_digits=10, decimal_places=2)