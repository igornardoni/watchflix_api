from django.test import TestCase
from watchflix.models import Programa


class FixtureDataTestCase(TestCase):

    fixtures = ['programas_iniciais']

    def test_fixture_load(self):
        serie_chaves = Programa.objects.get(pk=2)
        todos_programas = Programa.objects.all()
        self.assertEqual(serie_chaves.titulo, 'Chaves')
        self.assertEqual(len(todos_programas), 32)

