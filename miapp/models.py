from django.db import models
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_delete

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
    
@receiver(post_delete, sender=Producto)
def eliminar_imagen_producto(sender, instance, **kwargs):
    if instance.imagen:
        instance.imagen.delete(False)