from django.contrib.auth.models import User
from django.db import models
from .choices import *
# Create your models here.


class Noticias(models.Model):
    titulo_noticia = models.CharField(max_length=50)
    imagen_noticia = models.ImageField(upload_to='images/')
    descripcion_noticia = models.CharField(max_length=200)
    noticia_noticia = models.CharField(max_length=2000)

class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="images/", blank=True, null=True)

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=20)
    email_contacto = models.EmailField()
    tel_contacto = models.IntegerField()
    asunto_contacto = models.CharField(max_length=40)
    mensaje_contacto = models.CharField(max_length=500)

class Staff(models.Model):
    imagen_staff = models.ImageField(upload_to='images/')
    nombre_staff = models.CharField(max_length=20)
    descripcion_staff = models.CharField(max_length=200)
    
class Curso(models.Model):
    imagen_curso = models.ImageField(upload_to="images/")
    nombre_curso = models.CharField(max_length=40)
    descripcion_curso = models.CharField(max_length=300)
    descripcion_detalle_curso = models.CharField(max_length=600,default="Detalle")
    profesor_curso = models.CharField(max_length=30, default="profesor")
    precio_curso = models.IntegerField(max_length=5, default="0")
    #inscriptos

class TipoUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipousuario = models.CharField(max_length=150, choices=tipo_usuario)
    