from django.contrib import admin
from .models import Usuario, Amistad, Mensaje

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'email_institucional', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('nombres', 'apellidos', 'email_institucional')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    ordering = ('date_joined',)

@admin.register(Amistad)
class AmistadAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'estado', 'fecha_amistad')
    search_fields = ('user1__email_institucional', 'user2__email_institucional')
    list_filter = ('estado', 'fecha_amistad')
    ordering = ('fecha_amistad',)

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('remitente', 'destinatario', 'contenido', 'fecha_enviado')
    search_fields = ('remitente__email_institucional', 'destinatario__email_institucional', 'contenido')
    list_filter = ('fecha_enviado',)
    ordering = ('fecha_enviado',)
