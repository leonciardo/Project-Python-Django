from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Noticias
from .choices import *

from Academia_Arte.models import Avatar


class UserEditForm(forms.Form):

    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    imagen = forms.ImageField(label="Imagen")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class InscripcionFormulario(forms.Form):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido") 
    email = forms.EmailField(label="Email")
    curso = forms.ChoiceField(widget=forms.Select, choices=opcion_cursos)


class EditarNoticiaForm(forms.Form):
    titulo_noticia = forms.CharField(label="Titulo de la noticia")
    descripcion_noticia = forms.CharField(label="Descripcion de la noticia")
    noticia_noticia = forms.CharField(label="Noticia")
    imagen_noticia = forms.ImageField(label="Imagen")

    class Meta:
        model = Noticias
        fields = ['titulo_noticia', 'descripcion_noticia', 'noticia_noticia', 'imagen_noticia']
