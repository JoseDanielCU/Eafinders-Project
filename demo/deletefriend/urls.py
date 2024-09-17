from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name='home'),
    path('lista_amigos.html', views.lista_amigos, name='lista_amigos'),
    path('eliminar_amigo/<int:id>/', views.eliminar_amigo, name='eliminar_amigo'),
]