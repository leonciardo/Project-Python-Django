from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import update_session_auth_hash

from django.contrib import messages

# Create your views here.


# En la pantalla de inicio, Carga del modelo Noticias todas las noticias, y las devuelve en la vista de Inicio.
#Tambien se creo la carga de imagen del usuario Logueado
def VInicio(request):
    noticias = Noticias.objects.all()[:2]

    return render(request, "Academia_ArteApp/inicio.html",{"noticias":noticias})

#Se crea el formulario para el inicio de sesion.
#En caso de no existir el usuario que intenta loguearse renderisa nuevamente la pagina. En caso de loguear sesion, lo redirecciona a Inicio
def VLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")

            else:
                messages.error(request, "Usuario o contraseña incorrectos")
                return render(request, "Academia_ArteApp/login.html",{"form":form})

        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return render(request, "Academia_ArteApp/login.html", {"form": form})

    form = AuthenticationForm()
    return render(request, "Academia_ArteApp/login.html", {"form":form})

#Creamos formulario para registrar usuario, el cual luego de guardar, lo redirecciona a Login para que inicie sesion.
def VRegister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data["username"])
            avatar= Avatar(usuario=user, imagen="images/images/generic_user.png")
            avatar.save()

            return redirect("login")
        
        return render(request, "Academia_ArteApp/register.html",{"form":form})

    form = UserCreationForm()
    return render(request, "Academia_ArteApp/register.html",{"form":form})

def VLogout(request):
    logout(request)
    return redirect("inicio")

#Creamos formulario para la modificacion de los datos del perfil del usuario.
#Agregamos vista de Imagen de usuario dentro de la vista.
@login_required
def VPerfil(request):

    user = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.save()

            avatar = Avatar.objects.get(usuario=user)
            avatar.imagen = info=["imagen"]
            avatar.save()

            return redirect("inicio")

    else:
        form = UserEditForm(
            initial={
                "email": user.email, 
                "first_name": user.first_name, 
                "last_name": user.last_name,
                "imagen": user.avatar.imagen
                }) 


    return render(request, "Academia_ArteApp/edit_perfil.html",{"form":form})

@login_required
def VCambiarContra(request):

    user = request.user

    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            messages.success(request, ("Tu contraseña fue cambiada con exito!"))

            return redirect("inicio")

    else:
        form = PasswordChangeForm(user)

    return render(request, "Academia_ArteApp/cambiar_contra.html",{"form":form})



def VContacto(request):

    if request.method == 'POST':

        contacto_formulario = request.POST

        msj = Contacto(
            nombre_contacto=contacto_formulario["nombre_contacto"],
            email_contacto=contacto_formulario["email_contacto"],
            tel_contacto=contacto_formulario["tel_contacto"],
            asunto_contacto=contacto_formulario["asunto_contacto"],
            mensaje_contacto=contacto_formulario["mensaje_contacto"],
        )
        msj.save()
        return redirect("inicio")

    return render(request, "Academia_ArteApp/contacto.html")

def VAlumnos (request):

    return render (request, "Academia_ArteApp/alumnos.html")

def VProfesores (request):

    profe = Profesores.objects.all()

    return render(request, "Academia_ArteApp/profesores.html",{"profe":profe})

def VCursos (request):

    cursos = Curso.objects.all()

    return render (request, "Academia_ArteApp/cursos.html", {"cursos":cursos})

def VAcerca_de (request):
    staff = Staff.objects.all()

    return render(request, "Academia_ArteApp/acerca_de.html", {"staff":staff})  

def VNoticias (request):
    noticias = Noticias.objects.all()

    return render (request, "Academia_ArteApp/noticias.html",{"noticias":noticias})

class CursoDetalle(DetailView):
    model = Curso
    template_name = "Academia_ArteApp/curso_detalle.html"

    def get_context_data(self, **kwargs):
        context = super(CursoDetalle, self).get_context_data(**kwargs)
        context["todos_cursos"] = Curso.objects.all()
        return context

class ProfesorDetalle(DetailView):
    model = Profesores
    template_name = "Academia_ArteApp/profesor_detalle.html"

def VPintaManos(request):

    return render(request, "Academia_ArteApp/pinta_manos.html")

@staff_member_required
def VCrearNoticia(request):

    if request.method=="POST":

        noticia_form = request.POST
        imagen_form = request.FILES

        noticia = Noticias(
            titulo_noticia=noticia_form["titulo_noticia"],
            descripcion_noticia=noticia_form["descripcion_noticia"],
            noticia_noticia=noticia_form["noticia_noticia"],
            imagen_noticia=imagen_form["imagen_noticia"],

        )
        noticia.save()
        return redirect("inicio")

    else:
        noticia_form = ()
        noticia = ()

    return render(request, "Academia_ArteApp/crear_noticia.html",{})

class NoticiasList(ListView):
    model = Noticias
    template_name = "Academia_ArteApp/lista_noticias.html"

def VEliminarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    noticia.delete()
    return redirect("inicio")
