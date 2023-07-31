from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jpkatona$pagina_web',
        'USER': 'jpkatona',
        'PASSWORD': 'Porsche810',
        'HOST': 'jpkatona.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
