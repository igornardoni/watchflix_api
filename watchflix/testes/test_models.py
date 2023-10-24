from django.test import TestCase
from watchflix.models import Programa


class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo='Star Wars - Episódio IV',
            data_lancamento='1977-05-25',
            
        )

    def test_programa(self):
        """Teste que verifica os atributos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, 'Star Wars - Episódio IV')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '1977-05-25')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)
