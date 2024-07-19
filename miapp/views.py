from django.shortcuts import render, redirect
from .models import *
from .forms import loginForm, userRegitration
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Inicio de sesión
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = loginForm

# Cerrar sesión
class CustomLogoutView(LogoutView):
    next_page = 'login'

@login_required
# Vista de inicio
def index_view (requeset):
    return render(requeset, 'miapp/home.html')

@login_required
# Vista de Registro de usuario
def registro_view (requeset):
    return render(requeset, 'Registration/registrar_usuario.html', {
        'formUser': userRegitration
        })
