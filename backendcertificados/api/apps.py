# Importa la clase 'AppConfig' de Django.
from django.apps import AppConfig

# Define una clase de configuración para la aplicación 'api'.
class ApiConfig(AppConfig):
    # Especifica el tipo de campo de clave primaria predeterminado.
    default_auto_field = 'django.db.models.BigAutoField'

    # Especifica el nombre de la aplicación.
    name = 'api'
