from django.shortcuts import render
# Instanciamos las vistas genéricas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instanciamos el modelo 'Author' para poder usarlo en nuestras Vistas CRUD
from .models import Author, Editorial, Book


# Nos sirve para redireccionar después de una acción revertiendo patrones de expresiones regulares
from django.urls import reverse

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# Llamamos a la clase 'Author' que se encuentra en nuestro archivo 'models.py'


class AuthorList(ListView):
    model = Author


class AuthorCreate(SuccessMessageMixin, CreateView):
    model = Author  # Llamamos a la clase 'Author' que se encuentra en nuestro archivo 'models.py'
    # Le decimos a Django que muestre todos los campos de la tabla 'author' de nuestra Base de Datos
    fields = "__all__"
    # Mostramos este Mensaje luego de Crear un Author
    success_message = 'Author %(name)s created successfully !'

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        # Redireccionamos a la vista principal 'author_list'
        return reverse('author_list')


class AuthorDetail(DetailView):
    model = Author  # Llamamos a la clase 'Author' que se encuentra en nuestro archivo 'models.py'


class AuthorUpdate(SuccessMessageMixin, UpdateView):
    model = Author  # Llamamos a la clase 'Author' que se encuentra en nuestro archivo 'models.py'
    # Le decimos a Django que muestre todos los campos de la tabla 'author' de nuestra Base de Datos
    fields = "__all__"
    # Mostramos este Mensaje luego de Editar un Author
    success_message = 'Author  %(name)s Update succesfully !'

    # Redireccionamos a la página principal luego de actualizar un registro
    def get_success_url(self):
        # Redireccionamos a la vista principal 'author_list'
        return reverse('author_list')


class AuthorDelete(SuccessMessageMixin, DeleteView):
    model = Author
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self):
        # Mostramos este Mensaje luego de Eliminar un Author
        success_message = 'Author  %(name)s Delete succesfully !'
        messages.success(self.request, (success_message))
        # Redireccionamos a la vista principal 'author_list'
        return reverse('author_list')


class EditorialList(ListView):
    model = Editorial


class EditorialCreate(SuccessMessageMixin, CreateView):
    model = Editorial
    fields = "__all__"
    success_message = 'Editorial %(name)s created successfully !'

    def get_success_url(self):
        return reverse('editorial_list')


class EditorialDetail(DetailView):
    model = Editorial


class EditorialUpdate(SuccessMessageMixin, UpdateView):
    model = Editorial
    fields = "__all__"
    success_message = 'Editorial  %(name)s Update succesfully !'

    def get_success_url(self):
        return reverse('editorial_list')


class EditorialDelete(SuccessMessageMixin, DeleteView):
    model = Editorial
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Editorial  %(name)s Delete succesfully !'
        messages.success(self.request, (success_message))
        return reverse('editorial_list')


class BookList(ListView):
    model = Book


class BookCreate(SuccessMessageMixin, CreateView):
    model = Book
    fields = "__all__"
    success_message = 'Book %(title)s created successfully !'

    def get_success_url(self):
        return reverse('book_list')


class BookDetail(DetailView):
    model = Book


class BookUpdate(SuccessMessageMixin, UpdateView):
    model = Book
    fields = "__all__"
    success_message = 'Book  %(title)s Update succesfully !'

    def get_success_url(self):
        return reverse('book_list')


class BookDelete(SuccessMessageMixin, DeleteView):
    model = Book
    fields = "__all__"

    def get_success_url(self):
        success_message = f'Book  {self.object.title} delete succesfully !'
        messages.success(self.request, (success_message))
        return reverse('book_list')


"""
ANTERIOR
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Book, Editorial, Author


def index(request):
    template = loader.get_template("books/index.html")
    context = {
        "num editorial": Editorial.objects.all().count(),
        "num author": Author.objects.all().count(),
        "number_books": Book.objects.count(),
        "book1": Book.objects.first(),
    }
    return HttpResponse(template.render(context, request))



def create_books(request):
    new_book = Book(title='a new book', page=444, edition_date="2024-07-01", editorial=1, author=1)
    new_book.save()



def show_books(request):
    template = loader.get_template("books/index.html")
    obj = Book.objects.all()
    context = {'obj': obj}
    return HttpResponse(template.render(context, request))
"""
