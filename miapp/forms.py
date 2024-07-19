from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Formulario de inicio de sesión
class loginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario', 
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'campo',
            'autofocus': True,
            'required': True,
        }))
    password = forms.CharField(
        label='Contraseña', 
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'campo',
            'required': True,
        }))
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)



# Formulario de registro de usuario
class userRegitration(forms.Form):
    first_name = forms.CharField(
        label='Nombres', 
        max_length=200, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombres',
            'class': 'campo',
            'autofocus': True,
            'required': True,
        }))
    last_name = forms.CharField(
        label='Apellidos',
        max_length=200, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Apellidos',
            'class': 'campo',
            'required': True,
        }))
    profile = forms.ImageField(
        label='Foto de Perfil',
        widget=forms.ClearableFileInput(attrs={
            'class': 'campo__image',
        }))
    dni = forms.CharField(
        label='Apellidos',
        widget=forms.TextInput(attrs={
            'placeholder': 'Cedula',
            'class': 'campo',
            'required': True,
        }))
    date_born = forms.CharField(
        widget=forms.DateInput(attrs={
            'class': 'campo__date',
            'required': True,
        }))
    email = forms.CharField(
        widget=forms.EmailField(attrs={
            'class': 'campo',
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'campo',
            'required': True,
        }))
    roles = {'docente':'Docente',
             'administrativo':'Personal Administrativo',
             'estudiante':'Estudiante'}
    
    rol = forms.ModelChoiceField(
        label = 'rol',
        widget=forms.Select(choices=roles))
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    
