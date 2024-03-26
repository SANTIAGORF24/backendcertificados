from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Federacion
from .serializers import FederacionSerializer
from rest_framework import viewsets

@api_view(['POST'])
def iniciar_sesion(request):
    try:
        # Obtiene los datos de nombre de usuario y contraseña de la solicitud.
        username = request.data.get('username')
        password = request.data.get('password')

        # Utiliza la función authenticate para verificar las credenciales.
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Intenta obtener el token existente del usuario.
            token, created = Token.objects.get_or_create(user=user)

            # Devuelve el token en la respuesta.
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Las credenciales son inválidas.
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        # Manejo de excepciones y devolución de respuesta en formato JSON.
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FederacionViewSet(viewsets.ModelViewSet):
    queryset = Federacion.objects.all()
    serializer_class = FederacionSerializer
