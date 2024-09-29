from django.contrib import admin
from .models import Usuario, Amistad

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'email_institucional', 'is_active', 'is_staff', 'date_joined')  # Campos a mostrar
    search_fields = ('nombres', 'apellidos', 'email_institucional')  # Campos buscables
    list_filter = ('is_active', 'is_staff')  # Filtros en la barra lateral

@admin.register(Amistad)
class AmistadAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'estado', 'fecha_amistad')  # Campos a mostrar
    search_fields = ('user1__nombres', 'user1__apellidos', 'user2__nombres', 'user2__apellidos')  # Búsqueda por nombres y apellidos
    list_filter = ('estado',)  # Filtros para el estado de la amistad
    ordering = ('-fecha_amistad',)  # Ordenar por fecha de amistad de más reciente a más antiguo
