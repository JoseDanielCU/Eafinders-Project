from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Inicio.html', views.home, name='home'),
    path('Gente.html', views.add, name='add'),
    path('Amigos.html', views.friends, name='friends'),
    path('add_friend/<int:person_id>/', views.add_friend, name='add_friend'),

    path('delete_friend/<int:friend_id>/', views.delete_friend, name='delete_friend')  # Nueva URL para eliminar amigos
]