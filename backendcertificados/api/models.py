from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Define una clase 'Usuario' que hereda de 'AbstractUser'.
class Usuario(AbstractUser):
    # Puedes agregar campos adicionales aquí si es necesario.
    # Por ejemplo:
    # date_of_birth = models.DateField(null=True, blank=True)

    # Método que devuelve una representación en cadena del objeto 'Usuario'.
    def __str__(self):
        return self.username


class Federacion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nit = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

