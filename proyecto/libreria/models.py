from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    paginas = models.IntegerField()
    portada = models.ImageField(upload_to='portadas/')
    fecha_publicacion = models.DateField()