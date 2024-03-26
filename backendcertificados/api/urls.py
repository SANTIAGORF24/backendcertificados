# Importa la función 'path' y la vista 'iniciar_sesion' desde el módulo views del mismo directorio.
from django.urls import path, include
from .views import iniciar_sesion
from rest_framework.routers import DefaultRouter
from .views import FederacionViewSet

router = DefaultRouter()
router.register(r'federaciones', FederacionViewSet)

# Lista de patrones de URL específicos para la aplicación 'api'.
urlpatterns = [
    # Define una ruta para la vista 'iniciar_sesion'. Cuando se accede a 'iniciar_sesion/', se ejecuta la vista.
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('federaciones/', FederacionViewSet.as_view({'get': 'list'}), name='federacion-list'),

    # Puedes agregar más URLs según sea necesario para otras vistas.
]
