"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', VInicio, name='inicio'),
    path('login', VLogin, name='login'),
    path('register', VRegister, name='register'),
    path('logout', VLogout, name='logout'),
    path('cambiar_contra', VCambiarContra, name='cambiar_contra'),
    path('perfil', VPerfil, name='perfil'),
    path('cambiar_contra', VCambiarContra, name='cambiar_contra'),
    path('pinta_manos', VPintaManos, name='pinta_manos'),
    path('contacto', VContacto, name='contacto'),
    path('confirm_contacto', Vconfirm_contacto, name='confirm_contacto'),
    path('cursos', VCursos, name='cursos'),
    path('profesores', VProfesores, name='profesores'),
    path('acerca_de', VAcerca_de, name='acerca_de'),
    path('noticias', VNoticias, name ='noticias'),

    #Cursos CRUD
    path(r'curso/^(?P<pk>\d+)$', CursoDetalle.as_view(), name ='Detail'),
    path(r'curso/^nuevo$', CursoCreacion.as_view(), name ='nuevo_curso'),
    path('curso/list', CursoList.as_view(), name ='lista_cursos'),
    path(r'curso/^editar/(?P<pk>\d+)$', CursoUpdate.as_view(), name ='editar_curso'),
    path(r'curso/^eliminar(?P<pk>\d+)$', CursoDelete.as_view(), name ='eliminar_curso'),
    path('confirm_registro', Vconfirm_registro, name= 'confirm_registro'),

    #Noticias CRUD
    path('crear_noticia', VCrearNoticia, name='crear_noticia'),
    path('eliminar_noticia/<int:id>', VEliminarNoticia, name="eliminar_noticia"),
    path('editar_noticia/<int:id>', VEditarNoticia, name="editar_noticia"),
    path('lista_noticias', NoticiasList.as_view(), name='lista_noticias'),
    path('inscripcion_curso', VInscripcionCurso, name="inscripcion_curso"),
    path(r'noticias^(?P<pk>\d+)$', NoticiaDetalle.as_view(), name ='Detalle'),
    
    path(r'profesor/^(?P<pk>\d+)$', ProfesorDetalle.as_view(), name='profesor'),
  
    #Alumnos CRUD
    path('estudiantes_list', EstudiantesList.as_view(), name="estudiantes_list"),
    path(r'^(?P<pk>\d+)$', EstudianteDetail.as_view(), name="estudiante_detail"),
    path(r'^nuevo$', EstudianteCreate.as_view(), name="estudiante_create"),
    path(r'^editar/(?P<pk>\d+)$', EstudianteUpdate.as_view(), name="estudiante_update"),
    path(r'^eliminar/(?P<pk>\d+)$', EstudianteDelete.as_view(), name="estudiante_delete"),

    #Contacto CRUD
    path('mensajes_contacto', ContactoList.as_view(), name="mensajes_contacto"),
    path(r'eliminar_contacto/^(?P<pk>\d+)$',
         ContactoDelete.as_view(), name="mensaje_eliminar"),
    path(r'contacto_detalle/^(?P<pk>\d+)$',
         ContactoDetail.as_view(), name="mensaje_detail"),



]
