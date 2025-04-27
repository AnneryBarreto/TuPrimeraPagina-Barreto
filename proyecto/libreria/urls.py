from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='inicio'), 
    path('listar_libros/', views.listar_libros, name='listar_libros'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
]