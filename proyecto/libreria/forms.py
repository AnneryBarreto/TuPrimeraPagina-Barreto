from django import forms
from proyecto.libreria.models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'paginas', 'fecha_publicacion', 'descripcion', 'precio']