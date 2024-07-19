# miapp/urls.py
from django.urls import path
from .views import CustomLoginView, CustomLogoutView
from . import views

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('', views.index_view, name='home'),
    path('registro', views.registro_view, name='registro'),
]


