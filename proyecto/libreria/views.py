from django.shortcuts import  render, redirect
from .models import Libro
from .forms import LibroForm
from django.shortcuts import render

def base(request):
    return render(request, 'libreria/base.html')

def listar_libros(request):
    libros = Libro.objects.all() 
    return render(request, 'libreria/listar_libros.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libreria/agregar_libro.html', {'form': form})