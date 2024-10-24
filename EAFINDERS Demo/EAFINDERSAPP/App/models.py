from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone

class Amistad(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='amigos_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='amigos_user2', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')], default='pendiente')
    fecha_amistad = models.DateTimeField(auto_now_add=True)

    def enviar_solicitud(self):
        # Verifica que no exista una amistad o solicitud pendiente
        if not Amistad.objects.filter(
            Q(user1=self.user1, user2=self.user2) | Q(user1=self.user2, user2=self.user1)
        ).exists():
            self.save()  # Guarda la solicitud

    def aceptar_solicitud(self):
        self.estado = 'aceptada'
        self.save()

    def rechazar_solicitud(self):
        self.estado = 'rechazada'
        self.save()

    def delete(self, *args, **kwargs):
        # Elimina amistades relacionadas
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'Amistad entre {self.user1} y {self.user2} - {self.estado}'

class UsuarioManager(BaseUserManager):
    def create_user(self, email_institucional, password=None, **extra_fields):
        if not email_institucional:
            raise ValueError('El correo electrónico es obligatorio')

        email_institucional = self.normalize_email(email_institucional)
        user = self.model(email_institucional=email_institucional, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_institucional, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email_institucional, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email_institucional = models.EmailField(
        unique=True,
        validators=[RegexValidator(regex=r'^[\w\.-]+@eafit\.edu\.co$', message="El correo debe terminar en @eafit.edu.co")]
    )
    password = models.CharField(max_length=128)
    foto_perfil = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    carrera = models.CharField(max_length=100, blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email_institucional'
    REQUIRED_FIELDS = ['nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres} {self.apellidos} ({self.email_institucional})'

class Mensaje(models.Model):
    remitente = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_enviado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.remitente} a {self.destinatario}'
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  # Nombre de la etiqueta

    def __str__(self):
        return self.nombre

class Foro(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    foto_foro = models.ImageField(upload_to='foros_media/', blank=True, null=True)
    likes = models.ManyToManyField(Usuario, related_name='foros_likes', blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, related_name='foros', blank=True)  # Nuevo campo de etiquetas

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')
    archivo = models.FileField(upload_to='comentarios_archivos/', blank=True, null=True)  # Campo para archivos adjuntos

    def __str__(self):
        return f'Comentario de {self.autor} en {self.foro}'
