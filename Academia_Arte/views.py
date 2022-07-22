from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
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

class StaffRequiredMixin(object):

    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)


# En la pantalla de inicio, Carga del modelo Noticias todas las noticias, y las devuelve en la vista de Inicio.
#Tambien se creo la carga de imagen del usuario Logueado
def VInicio(request):
    noticias = Noticias.objects.all()[:2]

    return render(request, "Academia_Arte/inicio.html",{"noticias":noticias})

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
                return render(request, "Academia_Arte/login.html", {"form":form})

        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return render(request, "Academia_Arte/login.html", {"form":form})

    form = AuthenticationForm()
    return render(request, "Academia_Arte/login.html", {"form":form})

#Creamos formulario para registrar usuario, el cual luego de guardar, lo redirecciona a Login para que inicie sesion.
def VRegister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save() # guardamos el usuario
            user = User.objects.get(username=form.cleaned_data["username"])
            avatar = Avatar(usuario=user, imagen="images/generic_user.png")
            avatar.save()

            return redirect("login")
        
        return render(request, "Academia_Arte/register.html",{"form":form})

    form = UserCreationForm()

    return render(request, "Academia_Arte/register.html",{"form":form})

def VLogout(request):
    logout(request)
    return redirect("inicio")

#Creamos formulario para la modificacion de los datos del perfil del usuario.
#Agregamos vista de Imagen de usuario dentro de la vista.
@login_required
def VPerfil(request):

    user = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES)

        if form.is_valid():
            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.save()

            avatar = Avatar.objects.get(usuario=user)
            avatar.imagen = info["imagen"]
            avatar.save()

            return redirect("inicio")

    else:
        form = UserEditForm(initial={
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "imagen": user.avatar.imagen
        })

    return render(request, "Academia_Arte/edit_perfil.html",{"form":form})

@login_required
def VCambiarContra(request):

    user = request.user

    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            messages.success(request, "Your password has been changed successfully!")

            return redirect("inicio")

    else:
        form = PasswordChangeForm(user)

    return render(request, "Academia_Arte/cambiar_contra.html",{"form":form})




#Seccion Estudiantes

class EstudiantesList(StaffRequiredMixin,ListView):

    model = Estudiante
    template_name = "Academia_Arte/estudiantes_list.html"

class EstudianteDetail(StaffRequiredMixin,DetailView):

    model = Estudiante
    template_name = "Academia_Arte/estudiante_detail.html"

class EstudianteCreate(StaffRequiredMixin,CreateView):

    model = Estudiante
    success_url = "/estudiantes_list"
    fields = ["nombre", "apellido", "email"]

class EstudianteUpdate(StaffRequiredMixin,UpdateView):

    model = Estudiante
    success_url = "/estudiantes_list" # atenciooooooooon!!!! a la primer /
    fields = ["nombre_estudiante", "apellido_estudiante", "email_estudiante", "dni_estudiante", "curso_estudiante"]

class EstudianteDelete(StaffRequiredMixin,DeleteView):

    model = Estudiante
    success_url = "/estudiantes_list" # atenciooooooooon!!!! a la primer /

@staff_member_required
def VAlumnos (request):

    return render (request, "Academia_Arte/alumnos.html")


#Seccion Profesores
def VProfesores (request):

    profe = Profesores.objects.all()

    return render(request, "Academia_Arte/profesores.html",{"profe":profe})

class ProfesorDetalle(DetailView):
    model = Profesores
    template_name = "Academia_Arte/profesor_detalle.html"




#Seccion Cursos

def VCursos (request):
    cursos = Curso.objects.all()

    return render (request, "Academia_Arte/cursos.html", {"cursos":cursos})

def VCursos_lista (request):
    render(request, "Academia_Arte/curso_list.html")

class CursoList(StaffRequiredMixin,ListView):
    
    model = Curso
    Template_name = "Academia_Arte/cursos_list.html"
    
class CursoDetalle(StaffRequiredMixin,DetailView):
    
    model = Curso
    template_name = "Academia_Arte/curso_detalle.html"
    
    def get_context_data(self, **kwargs):
        context = super(CursoDetalle, self).get_context_data(**kwargs)
        context['todos_cursos'] = Curso.objects.all()
        return context
    
class CursoCreacion(StaffRequiredMixin,CreateView):
    
    model = Curso
    success_url = "/cursos"
    fields =[
        'nombre_curso',
        'descripcion_curso',
        'descripcion_detalle_curso',
        'profesor_curso',
        'precio_curso',
        'imagen_curso'
    ]

class CursoUpdate(StaffRequiredMixin,UpdateView):
    
    model = Curso
    success_url = "/cursos"
    fields =[
        'nombre_curso',
        'descripcion_curso',
        'descripcion_detalle_curso',
        'profesor_curso',
        'precio_curso',
        'imagen_curso'
        ]
    
class CursoDelete(DeleteView):
    
    model = Curso
    success_url = "/cursos"
    
@login_required
def VInscripcionCurso(request):

    cursos = Curso.objects.all()
    form_inscripcion = InscripcionFormulario(request.POST)

    if request.method == 'POST':
        inscripcion_formulario = request.POST

        inscripcion = Estudiante(
            nombre_estudiante=inscripcion_formulario["nombre_estudiante"],
            apellido_estudiante=inscripcion_formulario["apellido_estudiante"],
            email_estudiante=inscripcion_formulario["email_estudiante"],
            dni_estudiante=inscripcion_formulario["dni_estudiante"],
            curso_estudiante=inscripcion_formulario["curso_estudiante"],
        )
        inscripcion.save()
        return redirect("confirm_registro")
        
    return render(request,'Academia_Arte/inscripcion_curso.html',{"form_inscripcion":form_inscripcion,"cursos":cursos})

def Vconfirm_registro(request):
    
    return render (request, "Academia_Arte\confirmacion_registro_cursos.html")

#Seccion Noticias
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

    return render(request, "Academia_Arte/crear_noticia.html",{})

class NoticiasList(StaffRequiredMixin,ListView):
    model = Noticias
    template_name = "Academia_Arte/lista_noticias.html"

class NoticiaDetalle(StaffRequiredMixin,DetailView):
    model = Noticias
    template_name = "Academia_Arte/noticia_detalle.html"

def VEliminarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    noticia.delete()
    return redirect("inicio")

def VEditarNoticia(request, id):
    noticia = Noticias.objects.get(id=id)

    if  request.method == "POST":
        noticia_form = request.POST
        imagen_form = request.FILES

        noticias = Noticias(
            titulo_noticia=noticia_form["titulo_noticia"],
            descripcion_noticia=noticia_form["descripcion_noticia"],
            noticia_noticia=noticia_form["noticia_noticia"],
            imagen_noticia=imagen_form["imagen_noticia"],
        )
        noticias.save()
        return redirect("inicio")

    return render(request, "Academia_Arte/editar_noticia.html",{"noticia":noticia})

def VNoticias (request):
    noticias = Noticias.objects.all()

    return render (request, "Academia_Arte/noticias.html",{"noticias":noticias})



#Seccion CONTACTO
class ContactoList(StaffRequiredMixin,ListView):
    model = Contacto
    template_name = "Academia_Arte/mensajes_contacto.html"

class ContactoDelete(StaffRequiredMixin,DeleteView):
    model = Contacto
    success_url = "/mensajes_contacto"

class ContactoDetail(StaffRequiredMixin,DetailView):
    model = Contacto
    template_name = "Academia_Arte/mensaje_contacto_detalle.html"

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
        return redirect("confirm_contacto")

    return render(request, "Academia_Arte/contacto.html")

def Vconfirm_contacto(request):
    return render (request, "Academia_Arte/confirmacion_mensaje.html")


#Varios
def VPintaManos(request):

    return render(request, "Academia_Arte/pinta_manos.html")

def VAcerca_de (request):
    staff = Staff.objects.all()

    return render(request, "Academia_Arte/acerca_de.html", {"staff":staff})  
