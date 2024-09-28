from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['email_institucional', 'nombres', 'apellidos', 'is_staff', 'is_active']
    search_fields = ['email_institucional', 'nombres', 'apellidos']
    ordering = ['email_institucional']
    fieldsets = (
        (None, {'fields': ('email_institucional', 'password')}),
        ('Información Personal', {'fields': ('nombres', 'apellidos', 'foto_perfil', 'biografia', 'carrera', 'semestre')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Usuario, UsuarioAdmin)
