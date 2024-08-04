from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, calificaciones

class adminUser(UserAdmin):
    list_display = ('dni', 'email', 'first_name', 'last_name', 'rol', 'is_staff')
    search_fields = ('dni', 'first_name', 'last_name', 'email')
    list_filter = ('rol', 'is_staff', 'is_superuser', 'is_active')
    list_per_page = 15

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'dni', 'email', 'rol', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(User, adminUser)
