from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .models import calificaciones

# Formulario de inicio de sesión
class loginForm(AuthenticationForm):
    username = forms.CharField(
        label='Cédula', 
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'Cédula',
            'class': 'campo',
            'autofocus': True,
            'required': True,
        })
    )
    password = forms.CharField(
        label='Contraseña', 
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'campo',
            'required': True,
        })
    )
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

# Formulario de registro de usuario
class userRegistration(forms.Form):
    dni = forms.CharField(
        label='Cédula',
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'Cédula',
            'class': 'campo',
            'autofocus': True,
            'required': True,
        })
    )

    first_name = forms.CharField(
        label='Nombres', 
        max_length=200, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombres',
            'class': 'campo',
            'autofocus': True,
            'required': True,
        })
    )
    
    last_name = forms.CharField(
        label='Apellidos',
        max_length=200, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Apellidos',
            'class': 'campo',
            'required': True,
        })
    )
    
    profile_picture = forms.ImageField(
        label='Foto de Perfil',
        widget=forms.ClearableFileInput(attrs={
            'class': 'campo__image',
            'required': False
        }))
    
    
    date_born = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'campo__date',
            'required': True,
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo Electrónico',
            'class': 'campo',
            'required': True,
        })
    )
    
    password = forms.CharField(
        label='Contraseña', 
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'campo',
            'required': True,
        })
    )
    
    roles = [
        ('docente', 'Docente'),
        ('administrativo', 'Personal Administrativo'),
        ('estudiante', 'Estudiante')
    ]
    
    rol = forms.ChoiceField(
        label='Rol',
        choices=roles,
        widget=forms.Select(attrs={
            'class': 'campo',
            'required': True,
        })
    )
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

# Si necesitas un formulario basado en el modelo
class userModel(forms.ModelForm):
    class Meta:
        model = User
        fields = ['dni', 'first_name', 'last_name', 'profile_picture', 'date_born', 'email', 'password', 'rol']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Contraseña',
                'class': 'campo',
                'required': True,
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'campo__image',
            }),
            'date_born': forms.DateInput(attrs={
                'type': 'date',
                'class': 'campo__date',
                'required': True,
            }),
        }

class calificacionForm(forms.ModelForm):
        
    tarea = forms.CharField(
        label='Tareas',
        max_length=80,
        widget=forms.TextInput(attrs={
             'placeholder': 'examen',
             'class': 'campo',
             'autofocus': True,
             'required' : True,
        })
    )

    class Meta:
        model = calificaciones
        fields = ['tarea', 'nota', 'fecha_entrega', 'comentario']