from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('registro/', views.registro_usuario, name='register'),
    path('login/', views.login, name='login'),
    path('api/logout/', views.logout_user, name='logout'),
    path('Cuenta/', views.account, name='Cuenta'),
    path('EditProfile/', views.EditProfile, name='EditProfile'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('Notificaciones/', views.Notificaciones, name='Notificaciones'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
