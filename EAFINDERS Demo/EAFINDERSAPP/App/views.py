from .models import Usuario, Amistad, Mensaje, Foro, Comentario
from django.contrib.auth import login as auth_login, authenticate, logout
from .forms import RegistroUsuarioForm, LoginForm, EditarPerfilForm, BuscarUsuarioForm, ForoForm, ComentarioForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

def logout_user(request):
    """View to log out the user."""
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to the login page
    return redirect('home')  # If not POST, redirect to home or another page

@login_required
def profile_view(request, user_id):
    profile_user = get_object_or_404(Usuario, id=user_id)

    # Verifica si ya hay una solicitud enviada o recibida
    solicitud_enviada = Amistad.objects.filter(user1=request.user, user2=profile_user, estado='pendiente').exists()
    solicitud_recibida = Amistad.objects.filter(user1=profile_user, user2=request.user, estado='pendiente').first()
    son_amigos = Amistad.objects.filter(
        (Q(user1=request.user) & Q(user2=profile_user)) |
        (Q(user1=profile_user) & Q(user2=request.user)),
        estado='aceptada'
    ).exists()

    contexto = {
        'profile_user': profile_user,
        'solicitud_enviada': solicitud_enviada,
        'solicitud_recibida': solicitud_recibida,  # Pasamos la solicitud recibida si existe
        'son_amigos': son_amigos,
    }

    return render(request, 'Profiles.html', contexto)


@login_required
def account(request):
    # Obtener las amistades donde el usuario sea user1 o user2 y la solicitud haya sido aceptada
    amistades = Amistad.objects.filter(
        Q(user1=request.user, estado='aceptada') | Q(user2=request.user, estado='aceptada')
    )

    amigos = []
    for amistad in amistades:
        # Si el usuario es user1, el amigo es user2, y viceversa
        if amistad.user1 == request.user:
            amigos.append(amistad.user2)
        else:
            amigos.append(amistad.user1)

    return render(request, 'Cuenta.html', {'amigos': amigos})


def home(request):
    """View to display home page with all users except the logged-in user."""
    users = Usuario.objects.exclude(id=request.user.id)
    return render(request, 'home.html', {'users': users})

@login_required
def EditProfile(request):
    usuario = request.user  # Get the current user

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()  # Save the changes
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('Cuenta')  # Redirect to user profile
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = EditarPerfilForm(instance=usuario)  # Initialize the form with the current user data

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

def buscar_usuarios(request):
    form = BuscarUsuarioForm(request.GET)
    usuarios = Usuario.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        carrera = form.cleaned_data.get('carrera')
        semestre = form.cleaned_data.get('semestre')

        if query:
            usuarios = usuarios.filter(
                Q(nombres__icontains=query) |
                Q(apellidos__icontains=query) |
                Q(email_institucional__icontains=query)
            )

        if carrera:
            usuarios = usuarios.filter(carrera=carrera)

        if semestre:
            usuarios = usuarios.filter(semestre=semestre)

    return render(request, 'buscar_usuarios.html', {'form': form, 'usuarios': usuarios})


@login_required
def enviar_solicitud_amistad(request, user_id):
    if request.method == 'POST':
        receiver = get_object_or_404(Usuario, id=user_id)

        # Verifica si ya existe una amistad o solicitud
        if not Amistad.objects.filter(
            (Q(user1=request.user) & Q(user2=receiver)) |
            (Q(user1=receiver) & Q(user2=request.user))
        ).exists():
            # Crea la solicitud de amistad en estado pendiente
            Amistad.objects.create(user1=request.user, user2=receiver, estado='pendiente')

        return redirect('profile', user_id=receiver.id)
    return redirect('home') # Redirect if not a POST

def aceptar_solicitud_amistad(request, solicitud_id):
    solicitud = get_object_or_404(Amistad, id=solicitud_id)
    solicitud.aceptar_solicitud()
    return redirect('Notificaciones')


@login_required
def rechazar_solicitud_amistad(request, solicitud_id):
    # Obtener la solicitud de amistad
    amistad = get_object_or_404(Amistad, id=solicitud_id, user2=request.user, estado='pendiente')

    # Eliminar la solicitud de amistad
    amistad.delete()

    messages.success(request, 'Solicitud de amistad rechazada. Ahora puedes enviar una nueva solicitud si lo deseas.')
    return redirect('Notificaciones')
@login_required
def eliminar_amistad(request, user_id):
    amigo = get_object_or_404(Usuario, id=user_id)
    amistad = Amistad.objects.filter(
        (Q(user1=request.user) & Q(user2=amigo)) | (Q(user1=amigo) & Q(user2=request.user))
    )
    if amistad.exists():
        amistad.delete()
        messages.success(request, f'Amistad eliminada con {amigo}.')
    else:
        messages.error(request, 'No tienes una amistad con este usuario.')

    return redirect('profile', user_id=user_id)

@login_required
def Notificaciones(request):
    # Get pending friendship requests for the current user
    solicitudes = Amistad.objects.filter(user2=request.user, estado='pendiente')

    contexto = {
        'solicitudes': solicitudes
    }
    return render(request, 'Notificaciones.html', contexto)
@login_required
def chat_view(request, amigo_id):
    amigo = get_object_or_404(Usuario, id=amigo_id)

    # Verificar que son amigos
    amistad = Amistad.objects.filter(
        (Q(user1=request.user) & Q(user2=amigo)) | (Q(user1=amigo) & Q(user2=request.user)),
        estado='aceptada'
    ).exists()

    if not amistad:
        return redirect('home')  # Redirigir si no son amigos

    # Obtener los mensajes entre el usuario actual y el amigo
    mensajes = Mensaje.objects.filter(
        Q(remitente=request.user, destinatario=amigo) | Q(remitente=amigo, destinatario=request.user)
    ).order_by('fecha_enviado')

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            Mensaje.objects.create(remitente=request.user, destinatario=amigo, contenido=contenido)
            return redirect('chat_view', amigo_id=amigo.id)  # Redirigir para actualizar la conversación

    return render(request, 'chat.html', {'amigo': amigo, 'mensajes': mensajes})


@login_required
def obtener_mensajes(request, amigo_id):
    amigo = get_object_or_404(Usuario, id=amigo_id)

    # Obtener mensajes entre el usuario actual y el amigo
    mensajes = Mensaje.objects.filter(
        Q(remitente=request.user, destinatario=amigo) | Q(remitente=amigo, destinatario=request.user)
    ).order_by('fecha_enviado')

    # Formatear los mensajes para JSON
    mensajes_json = []
    for mensaje in mensajes:
        mensajes_json.append({
            'remitente': mensaje.remitente.nombres,  # Asegúrate de que este campo exista en tu modelo
            'contenido': mensaje.contenido,
        })

    return JsonResponse(mensajes_json, safe=False)
@login_required
def lista_conversaciones(request):
    # Obtener amigos con los que tienes amistad aceptada
    amigos = Amistad.objects.filter(
        (Q(user1=request.user) | Q(user2=request.user)),
        estado='aceptada'
    )
    return render(request, 'lista_Chats.html', {'amigos': amigos})


@login_required
def crear_foro(request):
    if request.method == 'POST':
        form = ForoForm(request.POST)
        if form.is_valid():
            foro = form.save(commit=False)
            foro.creador = request.user  # Asigna el usuario autenticado como creador
            foro.save()
            return redirect('detalle_foro', foro_id=foro.id)  # Redirige a la página del foro creado
    else:
        form = ForoForm()

    return render(request, 'crear_foro.html', {'form': form})
def detalle_foro(request, foro_id):
    foro = get_object_or_404(Foro, id=foro_id)
    comentarios = foro.comentarios.filter(parent=None)  # Solo comentarios principales (sin respuestas)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, request.FILES)  # Incluye request.FILES
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.foro = foro
            comentario.autor = request.user

            # Verifica si hay un parent_id en el POST (lo que indicaría una respuesta)
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comentario = get_object_or_404(Comentario, id=parent_id)
                comentario.parent = parent_comentario  # Asocia la respuesta al comentario principal

            comentario.save()
            return redirect('detalle_foro', foro_id=foro.id)
    else:
        form = ComentarioForm()

    return render(request, 'detalle_foro.html', {'foro': foro, 'comentarios': comentarios, 'form': form})

def lista_foros(request):
    foros = Foro.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_foros.html', {'foros': foros})


@login_required
def like_foro(request, foro_id):
    foro = get_object_or_404(Foro, id=foro_id)
    usuario = request.user

    if usuario in foro.likes.all():
        foro.likes.remove(usuario)  # Quitar el like si ya lo ha dado
    else:
        foro.likes.add(usuario)  # Añadir el like

    return redirect('lista_foros')

