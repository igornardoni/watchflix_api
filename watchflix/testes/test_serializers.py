from django.test import TestCase
from watchflix.models import Programa
from watchflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo='Star Wars - Episódio IV',
            data_lancamento='1977-05-25',
            tipo='F',
            likes=23540,
            dislikes=10
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_serializer(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_serializer_content(self):
        """Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)