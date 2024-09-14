from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Person, Friend


from django.shortcuts import render, redirect

def home(request):
    return render(request, 'Inicio.html')
def add(request):
    people = Person.objects.all()
    friends = Friend.objects.all()

    # Get a list of all the person IDs who are friends
    friends_ids = friends.values_list('person__id', flat=True)

    return render(request, 'Gente.html', {
        'people': people,
        'friends_ids': friends_ids
    })

def friends(request):
    friends = Friend.objects.all()
    return render(request, 'Amigos.html', {'friends': friends})

# View to add a person to friends
def add_friend(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    # Check if they are already a friend
    if not Friend.objects.filter(person=person).exists():
        Friend.objects.create(person=person)
    return redirect('friends')


def delete_friend(request, friend_id):
    # Verifica si el método es POST
    if request.method == 'POST':
        # Obtén el amigo que se desea eliminar o devuelve un error 404 si no existe
        friend = get_object_or_404(Friend, id=friend_id)
        friend.delete()  # Elimina al amigo de la base de datos
        messages.success(request, 'Amigo eliminado exitosamente.')

    # Redirige de vuelta a la página de amigos después de la eliminación
    return redirect('friends')

