from .models import Amistad  # Asegúrate de que la importación es correcta

def notificaciones_count(request):
    if request.user.is_authenticated:
        # Obtener solicitudes de amistad pendientes para el usuario actual
        solicitudes = Amistad.objects.filter(user2=request.user, estado='pendiente')
        return {
            'notificaciones_count': solicitudes.count()  # Agregar el conteo al contexto
        }
    return {
        'notificaciones_count': 0  # Retornar 0 si el usuario no está autenticado
    }
