from django import forms
from django.utils.translation import gettext_lazy as _
from proyecto.libreria.models import Libro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'paginas', 'fecha_publicacion', 'descripcion', 'precio', 'portada']

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']