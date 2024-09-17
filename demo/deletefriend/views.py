from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from .models import Amigo

# Create your views here.
def home(request):
    return render(request, 'home.html')

def eliminar_amigo(request, id):
    amigo_obj = get_object_or_404(Amigo, id=id)
    amigo_obj.delete()
    return redirect('lista_amigos')

def lista_amigos(request):
    amigos = Amigo.objects.all()
    return render(request, 'lista_amigos.html', {'amigos': amigos})
