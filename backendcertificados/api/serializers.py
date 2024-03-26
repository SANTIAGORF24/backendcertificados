# Importa la clase 'serializers' de Django REST framework y el modelo 'Usuario' desde el mismo directorio.
from rest_framework import serializers
from .models import Usuario
from .models import Federacion


# Define un serializador para el modelo 'Usuario'.
class UsuarioSerializer(serializers.ModelSerializer):
    # Metaclase que proporciona información sobre el modelo y los campos que deben serializarse.
    class Meta:
        # Especifica el modelo al que está asociado este serializador.
        model = Usuario

        # Lista de campos del modelo 'Usuario' que se incluirán en la serialización.
        fields = ['id', 'username', 'password']

class FederacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federacion
        fields = ['id', 'name', 'nit', 'domicilio', 'status', 'representante']