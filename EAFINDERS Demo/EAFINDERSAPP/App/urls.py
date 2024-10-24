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
    path('buscar/', views.buscar_usuarios, name='buscar_usuarios'),
    path('enviar_solicitud_amistad/<int:user_id>/', views.enviar_solicitud_amistad,name='enviar_solicitud_amistad'),
    path('aceptar_solicitud_amistad/<int:solicitud_id>/', views.aceptar_solicitud_amistad,name='aceptar_solicitud_amistad'),
    path('rechazar_solicitud_amistad/<int:solicitud_id>/', views.rechazar_solicitud_amistad, name='rechazar_solicitud_amistad'),
    path('eliminar_amistad/<int:user_id>/', views.eliminar_amistad, name='eliminar_amistad'),
    path('conversaciones/', views.lista_conversaciones, name='lista_conversaciones'),
    path('chat/<int:amigo_id>/', views.chat_view, name='chat_view'),
    path('chat/<int:amigo_id>/obtener-mensajes/', views.obtener_mensajes, name='obtener_mensajes'),
    path('crear_foro/', views.crear_foro, name='crear_foro'),
    path('foro/<int:foro_id>/', views.detalle_foro, name='detalle_foro'),
    path('foros/', views.lista_foros, name='lista_foros'),
    path('foros/<int:foro_id>/like/', views.like_foro, name='like_foro'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
