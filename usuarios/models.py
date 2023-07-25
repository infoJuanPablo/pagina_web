from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=12)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    es_colaborador = models.BooleanField(default=False)
    imagen_perfil = models.ImageField(upload_to = 'imagen_perfil',null=True,blank=True)
    numero_de_tarjeta = models.IntegerField(max_length=16, null=True) # aparentemente cuando usamos IntegerField ignora max_length
