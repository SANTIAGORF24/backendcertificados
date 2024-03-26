# Importa las funciones 'admin' y 'path' de los módulos correspondientes de Django.
from django.contrib import admin
from django.urls import path, include

# Lista de patrones de URL para el proyecto Django.
urlpatterns = [
    # Ruta para la interfaz de administración de Django.
    path('admin/', admin.site.urls),

    # Ruta para incluir las URL de la aplicación personalizada llamada 'api'.
    path('api/', include('api.urls')),
]
