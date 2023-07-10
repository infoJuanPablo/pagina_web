from django.contrib import admin
from .models import Publicaciones
from .models import Categoria

# Register your models here.

admin.site.register(Publicaciones)
admin.site.register(Categoria)