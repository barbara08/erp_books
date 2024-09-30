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
        self.assertEqual(self.editorial.num_books(), 0)


class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Marta")

    def test_str_method(self):
        self.assertEqual(str(self.author), "Marta")


class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="El libro de la selva", page=36, edition_date="oct. 6, 1926", Editorial="Anaya", author="Marta")

    def test_str_method(self):
        self.assertEqual(str(self.book), "El libro de la selva", 36)

    def gtest_was_published_recently(self):
        self.assertEqual(self.book.was_published_recently(), True)
