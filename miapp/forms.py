from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import User, calificacion, asignatura

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
class updateUserForm(forms.ModelForm):
    dni = forms.CharField(
        label='Número de cédula',
        validators=[RegexValidator(regex=r'^\d{10}$', message='El número de cédula debe tener exactamente 10 dígitos')],
        widget=forms.TextInput(attrs={
            'placeholder': 'Cédula',
            'class': 'campo',
            'required': True,
        }),
        error_messages={
            'invalid': 'Ingrese un número de cédula válido',
        }
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'campo',
            'required': True,
        }),
        validators=[validate_password]
    )
    class Meta:
        model = User
        fields = ['dni', 'first_name', 'last_name', 'profile_picture', 'date_born', 'email', 'password', 'rol']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Nombres',
                'class': 'campo',
                'autofocus': True,
                'required': True,
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Apellidos',
                'class': 'campo',
                'required': True,
            }),
            
            'profile_picture': forms.ClearableFileInput(attrs={
                'type': 'file',
                'class': 'campo__image',
                'required': False
            }),
            
            'date_born': forms.DateInput(attrs={
                'type': 'date',
                'class': 'campo__date',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'campo',
                'placeholder': 'Correo Electrónico'
            }),
            'rol': forms.Select(choices={
                ('docente', 'Docente'),
                ('administrativo', 'Personal Administrativo'),
                ('estudiante', 'Estudiante')
            }, attrs={
                'class': 'campo',
                'required': True,
            })
        }
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'profile_picture': 'Foto de perfil',
            'date_born': 'Fecha de nacimiento',
            'email': 'Correo Electrónico',
            'rol': 'Rol'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name'].strip().upper()
        user.last_name = self.cleaned_data['last_name'].strip().upper()
        user.username = f"{user.first_name} {user.last_name}"
        
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        return user

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
    nota = forms.IntegerField(
        label='Nota',
        widget=forms.NumberInput(attrs={
            'placeholder': 'nota',
            'class': 'campo',
            'required': True,
        })
    )
    fecha_entrega = forms.DateField(
        label='Fecha Entrega',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'campo__date',
            'required': True,
        })
    )
    
    asignatura = forms.ModelChoiceField(
        queryset=asignatura.objects.all(),
        label='Asignatura',
        widget=forms.Select(attrs={
            'class': 'campo',
            'placeholder': 'Selecionar',
            'required': True,
        })
    )
   

    class Meta:
        model = calificacion
        fields = ['tarea', 'nota', 'fecha_entrega', 'comentario', 'asignatura']



#formulario de asignatura
class asignaturaForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre de la Asignatura',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre de la Asignatura',
            'class': 'campo',
            'required': True,
        })
    )
    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={
            'placeholder': 'Descripción de la Asignatura',
            'class': 'campo',
            'required': True,
            'rows': 5,
        })
    )
    creditos = forms.IntegerField(
        label='Créditos',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Créditos',
            'class': 'campo',
            'required': True,
        })
    )
    curso = forms.CharField(
        label='Curso de la Asignatura',
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Curso de la Asignatura',
            'class': 'campo',
            'required': True,
        })
    )

    class Meta:
        model = asignatura
        fields = ['nombre', 'descripcion', 'creditos', 'curso']