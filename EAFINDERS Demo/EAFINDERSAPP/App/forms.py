
from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario



class LoginForm(forms.Form):
    email_institucional = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                                           label="Correo Institucional")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Contraseña")
class RegistroUsuarioForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar password")

    SEMESTRE_CHOICES = [(i, str(i)) for i in range(1, 11)]  # Opciones de 1 a 10
    CARRERA_CHOICES = [
        ('Ingenieria de Sistemas', 'Ingenieria de Sistemas'),
        ('Ingenieria de Diseño de Producto', 'Ingenieria de Diseño de Producto'),
        ('Ingenieria Mecanica', 'Ingenieria Mecanica'),
        ('Ingenieria Fisica', 'Ingenieria Fisica'),
        ('Ingenieria Matematica', 'Ingenieria Matematica'),
        ('Ingenieria Civil', 'Ingenieria Civil'),
        ('Gastronomia', 'Gastronomia'),
        ('Psicologia', 'Psicologia'),
        ('Geologia', 'Geologia'),
        ('Musica', 'Musica'),
        ('Negocios Internacionales', 'Negocios Internacionales'),
        ('Biologia', 'Biologia'),
        ('Comunicación Social', 'Comunicación Social'),
        ('Derecho', 'Derecho'),
        ('Economia', 'Economia'),
    ]

    carrera = forms.ChoiceField(choices=CARRERA_CHOICES, label="Carrera")
    semestre = forms.ChoiceField(choices=SEMESTRE_CHOICES, label="Semestre")

    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'email_institucional', 'password', 'confirm_password', 'foto_perfil',
                  'biografia', 'carrera', 'semestre']
        widgets = {
            'password': forms.PasswordInput(),  # Para asegurar que el password sea oculto
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'foto_perfil', 'biografia', 'carrera', 'semestre']  # Campos que se pueden editar
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(EditarPerfilForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})  # Estilos para cada campo
