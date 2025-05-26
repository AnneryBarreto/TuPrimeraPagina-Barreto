from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def perfil_completo_requerido(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, 'perfil'):
            return redirect('editar_perfil')
        return view_func(request, *args, **kwargs)
    return wrapper