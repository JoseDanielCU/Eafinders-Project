from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.conf import settings


class UsuarioManager(BaseUserManager):
    def create_user(self, email_institucional, password=None, **extra_fields):
        if not email_institucional:
            raise ValueError('El correo electrónico es obligatorio')

        email_institucional = self.normalize_email(email_institucional)
        user = self.model(email_institucional=email_institucional, **extra_fields)
        user.set_password(password)  # Hasheamos la contraseña
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
        validators=[
            RegexValidator(
                regex=r'^[\w\.-]+@eafit\.edu\.co$',
                message="El correo debe terminar en @eafit.edu.co"
            )
        ]
    )
    password = models.CharField(max_length=128)
    foto_perfil = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    carrera = models.CharField(max_length=100, blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)

    is_active = models.BooleanField(default=True)  # Campo necesario para el sistema de usuarios
    is_staff = models.BooleanField(default=False)  # Define si el usuario puede acceder al admin
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()  # Vinculamos el manager personalizado

    USERNAME_FIELD = 'email_institucional'  # Usamos el correo como nombre de usuario
    REQUIRED_FIELDS = ['nombres', 'apellidos']  # Campos obligatorios aparte de USERNAME_FIELD

    def __str__(self):
        return f'{self.nombres} {self.apellidos} ({self.email_institucional})'

