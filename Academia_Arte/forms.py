from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .choices import *

from Academia_Arte.models import Avatar


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput, required=False)  # la contraseña no se vea
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(label="Imagen")

    class Meta:
        model = Avatar
        fields = ["imagen"]

