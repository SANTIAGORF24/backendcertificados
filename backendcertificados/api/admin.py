from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Usuario
from .models import Federacion
class CustomUserAdmin(UserAdmin):
    # Campos adicionales que quieres mostrar en el admin
    list_display = ('username', 'email', 'date_joined', 'is_staff')

    # Configuración de la búsqueda en el admin
    search_fields = ('username', 'email')

    # Configuración de la edición en el admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información Personal'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permisos'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Fechas Importantes'), {'fields': ('last_login', 'date_joined')}),
    )

    # Configuración de los filtros en el admin
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Otros ajustes según tus necesidades

# Registrando el modelo personalizado con el administrador personalizado
admin.site.register(Usuario, CustomUserAdmin)

class FederacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'nit', 'domicilio', 'status', 'representante', 'created_at']
    # Puedes personalizar la visualización en el panel de administración según tus necesidades.

# Registra el modelo Federacion con su administrador personalizado.
admin.site.register(Federacion, FederacionAdmin)