from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    paginas = models.IntegerField(default=100)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    fecha_publicacion = models.DateField(default=date.today)
    descripcion = models.TextField()

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.titulo} - {self.portada}"

    
from django.db import models

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='avatars/', null=True, blank=True)
    password = models.CharField(max_length=128, default='default_password')
    username = models.CharField(max_length=150, unique=True, default='usuario_default')

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuario_groups"
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuario_permissions"
    )