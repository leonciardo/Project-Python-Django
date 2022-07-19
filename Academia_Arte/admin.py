from django.contrib import admin
from .models import *

# Register your models here.


class NoticiasAdmin(admin.ModelAdmin):
   list_display = (
       "titulo_noticia",
       "descripcion_noticia",
       "noticia_noticia",
       "imagen_noticia",
   )

   search_fields = (
       "titulo_noticia",
       "descripcion_noticia",
       "noticia_noticia",
       "imagen_noticia",
   )

class ContactoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_contacto",
        "email_contacto",
        "tel_contacto",
        "asunto_contacto",
        "mensaje_contacto",
    )
    search_fields = (
        "nombre_contacto",
        "email_contacto",
        "tel_contacto",
        "asunto_contacto",
        "mensaje_contacto",
    )
    
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_staff",
        "imagen_staff",
        "descripcion_staff",
        
    )
    search_fields = (
        "nombre_staff",
        "imagen_staff",
        "descripcion_staff",
    )

class CursoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_curso",
        "imagen_curso",
        "descripcion_curso",
        
    )
    search_fields = (
        "nombre_curso",
        "imagen_curso",
        "descripcion_curso",
    )


class ProfesoresAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_profesor",
        "apellido_profesor",
        "curso_profesor",

    )
    search_fields = (
        "nombre_profesor",
        "apellido_profesor",
        "curso_profesor",
    )

class EstudianteAdmin(admin.ModelAdmin):

    list_display = ('nombre_estudiante', 'apellido_estudiante', 'dni_estudiante', 'email_estudiante', 'curso_estudiante',)
    search_fields = (
        'nombre_estudiante', 'apellido_estudiante', 'dni_estudiante', 'email_estudiante', 'curso_estudiante',) 
   

admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Avatar)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(TipoUsuario)
admin.site.register(Profesores,ProfesoresAdmin)
admin.site.register(Estudiante,EstudianteAdmin)
