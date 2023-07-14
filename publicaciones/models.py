from django.db import models
from usuarios.models import Usuario
# Create your models here.
#esta clase crea una tabla para guardar categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)



    def __str__(self):
        return self.nombre







#esta clase crea una tabla para publicaciones
class Publicaciones(models.Model):
    fecha = models.DateField(auto_now_add= True)
    update = models.DateField(auto_now=True)
    titulo = models.CharField(max_length=255)
    post = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name= 'posteos', null=True)
    creador = models.ForeignKey(Usuario, on_delete= models.CASCADE, related_name='posteos_usuario', default=1)

    def __str__(self):
        return self.titulo
    


class Comentario(models.Model):
    
    fecha = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Publicaciones, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField(null=True)

    def __str__(self):
        return self.post.titulo + '-' + self.autor.first_name

