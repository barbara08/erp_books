# from django.shortcuts import render
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

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EditorialSerializer, AuthorSerializer, BookSerializer


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
        success_message = f'Author  {self.object.name} delete succesfully !'
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
        success_message = f'Editorial  {self.object.name} delete succesfully !'
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


# API


class EditorialListApiView(ListCreateAPIView):
    # 1. List all
    serializer_class = EditorialSerializer
    queryset = Editorial.objects.all()

    # 2. Create
    def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'),
        }
        serializer = EditorialSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditorialUpdateApiView(RetrieveUpdateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    partial = True


class EditorialDeleteApiView(DestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Editorial"))


class AuthorListApiView(ListCreateAPIView):
    # 1. List all
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    # 2. Create
    def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'),
        }
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorUpdateApiView(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    partial = True


class AuthorDeleteApiView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Author"))


class BookListApiView(ListCreateAPIView):
    # 1. List all
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    # 2. Create
    def post(self, request, *args, **kwargs):

        data = {
            'title': request.data.get('title'),
            'page': request.data.get('page'),
            'edition_date': request.data.get('edition_date'),
            'editorial': request.data.get('editorial'),
            'author': request.data.get('author'),
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateApiView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    partial = True


class BookDeleteApiView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Book"))


"""
class EditorialDetailApiView(APIView):

    def get_object(self, editorial_id):
        try:
            return Editorial.objects.get(id=editorial_id)
        except Editorial.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, editorial_id, *args, **kwargs):
        editorial_instance = self.get_object(editorial_id)
        if not editorial_instance:
            return Response(
                {"res": "Object with editorial id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EditorialSerializer(editorial_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, editorial_id, *args, **kwargs):

        editorial_instance = self.get_object(editorial_id)
        if not editorial_instance:
            return Response(
                {"res": "Object with editorial id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
        }
        serializer = EditorialSerializer(
            instance=editorial_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 5. Delete
    def delete(self, request, editorial_id, *args, **kwargs):
        editorial_instance = self.get_object(editorial_id)
        if not editorial_instance:
            return Response(
                {"res": "Object with editorial id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        editorial_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )




class AuthorListApiView(APIView):
    # 1. List all

    def get(self, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'),
        }
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailApiView(APIView):

    def get_object(self, author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, author_id, *args, **kwargs):
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AuthorSerializer(author_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, author_id, *args, **kwargs):

        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
        }
        serializer = AuthorSerializer(
            instance=author_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 5. Delete
    def delete(self, request, author_id, *args, **kwargs):
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        author_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )




class BookListApiView(APIView):
    # 1. List all
    def get(self, *args, **kwargs):

        books = Book.objects.all()
        # bookss = Book.objects.filter(editorial='editorial')
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):

        data = {
            'title': request.data.get('title'),
            'page': request.data.get('page'),
            'edition_date': request.data.get('edition_date'),
            'editorial': request.data.get('editorial'),
            'author': request.data.get('author'),
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookDetailApiView(APIView):

    def get_object(self, book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, book_id, *args, **kwargs):
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with book id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookSerializer(book_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, book_id, *args, **kwargs):

        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with book id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'page': request.data.get('page'),
            'edition_date': request.data.get('edition_date'),
            'editorial': request.data.get('editorial'),
            'author': request.data.get('author'),
        }
        serializer = BookSerializer(
            instance=book_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 5. Delete
    def delete(self, request, book_id, *args, **kwargs):
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with book id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        book_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
"""
