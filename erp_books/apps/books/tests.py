from django.test import TestCase
from .models import Editorial, Author, Book


# Create your tests here.

"""
El creado por mi
class EditorialModelTest(TestCase):
    def setUp(self):
        Editorial.objects.create(name='testEditorial')

    def ModelTestCreated(self):
        objet = Editorial.objects.get(name='testEditorial')

        self.assertEqual(objet.name, 'testEditorial')
"""


class EditorialModelTest(TestCase):
    def setUp(self):
        self.editorial = Editorial.objects.create(name="Anaya")

    def test_str_method(self):
        self.assertEqual(str(self.editorial), "Anaya (0)")
        self.assertEqual(self.editorial.get_num_books(), 0)
