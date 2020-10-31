from django.test import TestCase
import unittest
from .models import MisionVision, Insumos
from django.contrib.auth.models import User

# Create your tests here.
class TestUno(unittest.TestCase):

    def grabar_mision_y_vision(self):
        m = MisionVision(
            ident="dos", mision="nuestra mision...",vision="nuestra vision es"
        )
        valor=0
        try:
            m.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

        def listar_mision(self):
            lm= MisionVision.objects.all()
            self.assertIsInstanve(lm,MisionVision)

class TestDos(unittest.TestCase):

    def grabar_insumo(self):
        valor = 0
        try:
            i = Insumos(
                nombre = "Crema", precio = 1500, descripcion = "", stock = 50
            )
            i.save()
            valor = 1
        except:
            valor = 0
        self.assertIn(valor,1)

class testTres(unittest.TestCase):
    
    def grabar_usuario(self):
        valor = 0
        try:
            u = User(
                nombre = "Alberto",
                apellido = "Fuentes",
                email = "alfuentes@gmail.cl",
                usuario = "alfuentes",
                pass1 = "123456"
            )
            u.save()
            valor = 1
        except:
            calor = 0
        self.assertIn(valor,1)
    
if __name__ == "__main__":
    unittest.main()
    