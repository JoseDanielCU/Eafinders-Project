from .models import Usuario
from django.contrib.auth import login as auth_login, authenticate, logout
from .forms import RegistroUsuarioForm, LoginForm, EditarPerfilForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models

def logout_user(request):
    """View to log out the user."""
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to the login page
    return redirect('home')  # If not POST, redirect to home or another page

@login_required
def profile_view(request, user_id):
    """View to display a user's profile."""
    user = get_object_or_404(Usuario, id=user_id)
    return render(request, 'Profiles.html')
@login_required
def Notificaciones(request):
    """View to show notifications for friendship requests."""
    return render(request, 'notificaciones.html')

@login_required
def account(request):
    return render(request, 'Cuenta.html')
def home(request):
    """View to display home page with all users except the logged-in user."""
    users = Usuario.objects.exclude(id=request.user.id)
    return render(request, 'home.html', {'users': users})

@login_required
def EditProfile(request):
    usuario = request.user  # Obtenemos el usuario actual

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()  # Guardamos los cambios
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('Cuenta')  # Redirigir al perfil del usuario
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = EditarPerfilForm(instance=usuario)  # Inicializamos el formulario con los datos del usuario actual

    return render(request, 'EditProfile.html', {'form': form})

def login(request):
    """View for user login."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_institucional = form.cleaned_data['email_institucional']
            password = form.cleaned_data['password']

            # Authenticate using the email as the username
            usuario = authenticate(request, username=email_institucional, password=password)
            if usuario is not None:
                auth_login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Correo o contraseña incorrectos.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def registro_usuario(request):
    """View for user registration."""
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data['password'])  # Hash the password
            usuario.save()

            # Automatically authenticate the user after registration
            auth_login(request, usuario)
            return redirect('home')  # Redirect to the home page
    else:
        form = RegistroUsuarioForm()

    return render(request, 'Register.html', {'form': form})
