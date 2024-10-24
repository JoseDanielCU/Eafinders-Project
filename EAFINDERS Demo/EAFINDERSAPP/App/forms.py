from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario, Foro, Comentario

class BuscarUsuarioForm(forms.Form):
    query = forms.CharField(
        label='Buscar usuario',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre, apellido o email...'})
    )

    # Opciones para el filtro de carrera
    CARRERA_CHOICES = [
        ('', 'Todas las carreras'),
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

    SEMESTRE_CHOICES = [('', 'Todos los semestres')] + [(i, str(i)) for i in range(1, 11)]  # Opciones de 1 a 10

    carrera = forms.ChoiceField(
        choices=CARRERA_CHOICES,
        required=False,
        label='Carrera',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    semestre = forms.ChoiceField(
        choices=SEMESTRE_CHOICES,
        required=False,
        label='Semestre',
        widget=forms.Select(attrs={'class': 'form-select'})
    )


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
        fields = ['nombres', 'apellidos', 'foto_perfil', 'biografia', 'carrera', 'semestre']  # Campos que se pueden editar
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(EditarPerfilForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})  # Estilos para cada campo

class ForoForm(forms.ModelForm):
    class Meta:
        model = Foro
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del foro'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del foro'}),
        }
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Añade un comentario...'}),
        }