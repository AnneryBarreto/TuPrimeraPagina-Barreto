from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base, name='inicio'), 
    path('listar_libros/', views.listar_libros, name='listar_libros'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('libro/<int:pk>/editar/', views.editar_libro, name='editar_libro'),
    path('libro/<int:pk>/borrar/', views.borrar_libro, name='borrar_libro'),
    path('acerca/', views.acerca, name='acerca'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)