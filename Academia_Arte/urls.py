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
    path('pinta_manos', VPintaManos, name='pinta_manos'),
    path('contacto', VContacto, name='contacto'),
    path('cursos', VCursos, name='cursos'),
    path('alumnos', VAlumnos, name='alumnos'),
    path('profesores', VProfesores, name='profesores'),
    path('acerca_de', VAcerca_de, name='acerca_de'),
    path('noticias', VNoticias, name ='noticias'),
    path(r'curso/^(?P<pk>\d+)$', CursoDetalle.as_view(), name ='Detail'),#cursos/<pk>
    path(r'curso/^nuevo$', CursoCreacion.as_view(), name ='nuevo_curso'),
    path('curso/list', CursoList.as_view(), name ='lista_cursos'),
    path(r'curso/^editar/(?P<pk>\d+)$', CursoDetalle.as_view(), name ='editar_curso'),
    path(r'curso/^eliminar(?P<pk>\d+)$', CursoDetalle.as_view(), name ='eliminar_curso'),
    path('crear_noticia', VCrearNoticia, name='crear_noticia'),
    path('eliminar_noticia/<int:id>', VEliminarNoticia, name="eliminar_noticia"),
    path('lista_noticias', NoticiasList.as_view(), name='lista_noticias'),
    path('inscripcion_curso', VInscripcionCurso, name="inscripcion_curso"),
    path(r'noticias^(?P<pk>\d+)$', NoticiaDetalle.as_view(), name ='Detalle'),
    


]
