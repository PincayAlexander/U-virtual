from django.dispatch import receiver
from django.db import models


class usuario(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='perfil/')
    dni = models.CharField(max_length=20, unique=True)
    date_born = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    roles = {'docente':'Docente',
             'administrativo':'Personal Administrativo',
             'estudiante':'Estudiante'}
    rol = models.CharField(max_length=20, choices=roles)
    
    def __str__(self):
        return f"{self.dni}: {self.first_name} {self.last_name}"


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')