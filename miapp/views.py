from django.shortcuts import render, redirect
from .models import *
from .forms import updateUserForm, loginForm, calificacionForm, asignaturaForm
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
def index_view(request):
    links = [
        {'title': 'Asignatura', 'image': './img/cards/asignatura.png', 'url': 'asignatura'},
        {'title': 'Actividad', 'image': './img/cards/actividad.jpg', 'url': '#'},
        {'title': 'Calificaciones', 'image': './img/cards/calificacion.jpg', 'url': 'calificacion'},
        {'title': 'Horario', 'image': './img/cards/horario.png', 'url': '#'},
        {'title': 'Citación', 'image': './img/cards/citacion.jpeg', 'url': '#'},
        {'title': 'Tutoria', 'image': './img/cards/tutoria.jpg', 'url': '#'},
        {'title': 'Conducta', 'image': './img/cards/conducta.jpg', 'url': '#'},
        {'title': 'Usuario', 'image': './img/cards/usuario.png', 'url': 'updateUser'},
    ]
    return render(request, 'miapp/home.html', {'links': links})

@login_required
# Vista de actualización de usuario
def updateUser_view(request):
    if request.method == 'POST':
        userForm = updateUserForm(request.POST, request.FILES)
        if userForm.is_valid():
            user = userForm.save(commit=False)
            password = request.POST.get('password')
            if password:  # Verificar si se proporcionó una contraseña
                user.set_password(password)  # Hashear la contraseña antes de guardarla
            userForm.save()
            return redirect('home')
    else:
        userForm = updateUserForm()  # Inicializa el formulario si la solicitud no es POST

    return render(request, 'Registration/registrar_usuario.html', {
        'formUser': userForm
    })

@login_required
def calificacion_view(request):
    usuario = None
    if request.method == 'GET' and 'dni' in request.GET:
        dni = request.GET.get('dni')
        try:
            usuario = User.objects.get(dni=dni)
        except User.DoesNotExist:
            usuario = None

    if request.method == 'POST':
        Caliform = calificacionForm(request.POST, request.FILES)
        if Caliform.is_valid():
            Caliform.save()
            return redirect('home')
    else:
        Caliform = calificacionForm()
    
    return render(request, 'miapp/registrar_calificacion.html', {
        'formCali': Caliform,
        'usuario': usuario
    })

@login_required
def asignatura_view(request):
    if request.method == 'POST':
        asigForm = asignaturaForm(request.POST)
        if asigForm.is_valid():
            asigForm.save()
            return redirect('home')  
    else:
        asigForm = asignaturaForm()
    return render(request, 'miapp/registrar_asignatura.html', {
        'formAsig': asigForm
    })
