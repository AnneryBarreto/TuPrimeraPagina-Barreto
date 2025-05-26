from django.contrib.auth.mixins import LoginRequiredMixin

class RequiereLoginMixin(LoginRequiredMixin):
    """Este mixin hace que la vista requiera autenticación."""
    login_url = '/usuarios/login/'