from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

