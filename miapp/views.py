from django.shortcuts import render, redirect
from .models import *
from .forms import loginForm, userRegistration, userModel, calificacionForm
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
def registro_view(request):
    if request.method == 'POST':
        userRegistration = userModel(request.POST, request.FILES)
        if userRegistration.is_valid():
            userRegistration.save()
            return redirect('home')
    else:
        userRegistration = userModel()
    return render(request, 'Registration/registrar_usuario.html', {
        'formUser': userRegistration
    })

@login_required
def calificacion_view(request):
    if request.method == 'POST':
        form = calificacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = calificacionForm()
    
    return render(request, 'miapp/registrar_calificaciones.html', {
        'form': form
    })
