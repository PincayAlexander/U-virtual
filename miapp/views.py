from django.shortcuts import render
from .models import Producto

def home_view(request):
    productos = Producto.objects.all()
    return render(request, 'miapp/home.html', {'productos': productos})
