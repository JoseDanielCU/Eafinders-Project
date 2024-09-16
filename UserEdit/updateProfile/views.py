from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import UserRecords
from .forms import UsuarioForm

# Create your views here.
def editar_usuario(request):
    if request.method == 'POST':
        selected_user_id = request.POST.get('selected_user')
        username = request.POST.get('username')
        description = request.POST.get('desc')

        if selected_user_id:
            usuario = get_object_or_404(UserRecords, id=selected_user_id)
            # Actualiza la informacion de usuario
            usuario.username = username
            usuario.description = description
            usuario.save()
            # Redirige a la misma pagina
            return redirect('Usuarios')
    # Obtén todos los usuarios para las tarjetas
    usuarios = UserRecords.objects.all()
    return render(request, 'studentEdit.html', {'usuarios': usuarios})