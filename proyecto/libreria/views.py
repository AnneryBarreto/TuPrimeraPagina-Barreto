from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from proyecto.libreria.models import Libro
from proyecto.libreria.forms import LibroForm
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect
from proyecto.proyecto.mixins import RequiereLoginMixin
from .forms import RegistroUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .forms import ImagenPerfilForm
from .models import Usuario

def base(request):
    return render(request, 'base.html')

def acerca(request):
    return render(request, 'acerca.html')

@login_required
def listar_libros(request):
    libros = Libro.objects.all() 
    return render(request, 'libreria/listar_libros.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libreria/agregar_libro.html', {'form': form})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libreria/detalle_libro.html', {'libro': libro})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('detalle_libro', pk=libro.pk)
    return render(request, 'libreria/editar_libro.html', {'form': form})

def borrar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'libreria/borrar_libro.html', {'libro': libro})

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

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html', {'user': request.user})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})

def actualizar_imagen(request):
    if request.method == 'POST':
        form = ImagenPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ImagenPerfilForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})

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