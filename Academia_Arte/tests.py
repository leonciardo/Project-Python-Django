from django.test import TestCase
from .models import Curso
from django.urls import reverse
from . import views
# Create your tests here.

class AppTest(TestCase):
    
    def setUp(self):
        Curso.objects.create(nombre_curso="Curso de pintura", profesor_curso="pintor", precio_curso="500", descripcion_curso="curso de prueba",descripcion_detalle_curso="curso de prueba",imagen_curso="")
        

    def test_VInicio(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code,200)
        
    def test_CursoCreate(self):
        curso = Curso.objects.get(precio_curso=500)
        self.assertEqual(curso.nombre_curso,"Curso de pintura")