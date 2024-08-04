from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Modelo Usuario personalizado
class UserManager(BaseUserManager):
    def create_user(self, dni, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener una dirección de correo electrónico')
        user = self.model(dni=dni, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(dni, email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, blank=True)
    dni = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.ImageField(default='default.png', upload_to='perfil/')
    date_born = models.DateField(null=True, blank=True)
    
    roles = [('docente', 'Docente'),
        ('administrativo', 'Personal Administrativo'),
        ('estudiante', 'Estudiante')]
    
    rol = models.CharField(max_length=20, choices=roles)
    
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'dni'
    
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['dni', 'rol']


class calificaciones(models.Model):
    tarea = models.CharField(max_length=80)
    nota = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_entrega = models.DateField(null=True, blank=True)
    comentario =  models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.tarea} - {self.nota}"
    
    class Meta:
        verbose_name_plural = "Calificaciones"