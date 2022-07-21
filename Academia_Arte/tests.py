from django.test import TestCase
from .models import Curso, Profesores
from django.urls import reverse
from . import views
# Create your tests here.

class AppTest(TestCase):
    
    def setUp(self):
        Curso.objects.create(nombre_curso="Curso de pintura", profesor_curso="pintor", precio_curso="500", descripcion_curso="curso de prueba",descripcion_detalle_curso="curso de prueba",imagen_curso="")
        Profesores.objects.create(nombre_profesor="profesor",apellido_profesor=" de pintura de arte moderno y antiguo etc... udfhusdhfisudh", curso_profesor="Arte", descripcion_profesor="profesor de prueba",biografia_profesor="curso de prueba",imagen_profesor="")

    def test_VInicio(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code,200)
        
    def test_CursoCreate(self):
        curso = Curso.objects.get(precio_curso=500)
        self.assertEqual(curso.nombre_curso,"Curso de pintura")
        
    def test_VNoticias(self):
        response = self.client.get(reverse('noticias'))
        self.assertEqual(response.status_code,200)