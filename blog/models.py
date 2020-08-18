from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = 'blog', null= True, blank= True) #null y blank es para que no sea necesario ingresar imagen
    autor = models.ForeignKey(User, on_delete=models.CASCADE)#para eliminar todos los post cuando un usuario elimina su cuenta de la pagina, y para hacer una lista desplegable para elegir autor
    categorias = models.ManyToManyField(Categoria)#relacione la Clase Post con la Clase Categoria porque puede comparter varias categorias un post y viceversa
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.titulo