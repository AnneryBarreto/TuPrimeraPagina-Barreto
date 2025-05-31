from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from proyecto.libreria.models import Libro
from proyecto.libreria.forms import LibroForm
from django.shortcuts import render, redirect
from proyecto.proyecto.mixins import RequiereLoginMixin

def base(request):
    return render(request, 'base.html')

def acerca(request):
    return render(request, 'acerca.html')

def listar_libros(request):
    libros = Libro.objects.all() 
    return render(request, 'libreria/templates/libreria/listar_libros.html', {'libros': libros})

@login_required
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libreria/agregar_libro.html', {'form': form})

class LibroListView(ListView):
    model = Libro
    template_name = 'libreria/listar_libros.html'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libreria/detalle_libro.html'

class LibroProtectedView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'libreria/listar_libros.html'

class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'autor', 'paginas', 'portada', 'fecha_publicacion']
    template_name = 'crear_libro.html'

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['titulo', 'autor', 'paginas', 'portada', 'fecha_publicacion']
    template_name = 'editar_libro.html'

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'borrar_libro.html'
    success_url = '/'

class LibroListView(RequiereLoginMixin, ListView):
    model = Libro
    template_name = 'listar_libros.html'