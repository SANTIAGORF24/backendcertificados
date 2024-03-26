# Django settings for backendcertificados project.

# Importa la clase Path de la biblioteca pathlib para manejar rutas de archivos.
from pathlib import Path

# Define el directorio base del proyecto utilizando la ruta actual del archivo.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de desarrollo rápido - No recomendado para producción.
DEBUG = True
APPEND_SLASH = False


# Clave secreta de Django utilizada para operaciones criptográficas y de seguridad.
SECRET_KEY = 'django-insecure-+_02&7(v8curln_!(iyu8qb7^wxe15*v#u_%jmheje(u6$a$x+'

# Lista de hosts permitidos para la aplicación (vacía permite todos).
ALLOWED_HOSTS = []


# Lista de aplicaciones instaladas en el proyecto Django.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'corsheaders',
    'api',  # Aplicación personalizada llamada 'api'.
]

# Configuración del modelo de usuario personalizado.
AUTH_USER_MODEL = 'api.Usuario'

# Middleware utilizado por la aplicación para procesar las solicitudes y respuestas.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# Configuración del archivo de URL principal y seguridad de cookies.
ROOT_URLCONF = 'backendcertificados.urls'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Configuración de validación de contraseñas.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,  # Contraseñas deben tener al menos 8 caracteres.
        }
    },
]

# Configuración de plantillas para la aplicación Django.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de dominios permitidos para solicitudes CORS.
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Añade la URL de tu frontend
]

# Configuración de la aplicación WSGI (interfaz de aplicación web).
WSGI_APPLICATION = 'backendcertificados.wsgi.application'

# Configuración de la base de datos SQLite.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",  # Ruta del archivo de base de datos.
    }
}

# Configuración de validación de contraseñas (otra instancia).
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de internacionalización y zona horaria.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos (CSS, JavaScript, imágenes).
STATIC_URL = 'static/'

# Tipo de campo de clave primaria predeterminado.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
