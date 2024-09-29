from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db.models import Q
from django.conf import settings
from django.db import models
from django.conf import settings
from django.db.models import Q

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


