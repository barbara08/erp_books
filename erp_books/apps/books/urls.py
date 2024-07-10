from django.urls import path
from django.views.generic import TemplateView


from .views import (
    AuthorList,
    AuthorCreate,
    AuthorUpdate,
    AuthorDetail,
    AuthorDelete
)
from .views import (
    EditorialList,
    EditorialCreate,
    EditorialDetail,
    EditorialUpdate,
    EditorialDelete
)
from .views import (
    BookList,
    BookCreate,
    BookDetail,
    BookUpdate,
    BookDelete
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="index_ppal"),
    # path('', IndexView.as_view(template_name="index.html"), name="index_ppal"),
    path('authors/', AuthorList.as_view(template_name="authors/index.html"),
         name='author_list'),
    # La ruta 'create' en donde mostraremos un nuevo author o registro
    path('authors/create',
         AuthorCreate.as_view(template_name="authors/create.html"), name='author_create'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de los autores
    path('authors/detail/<int:pk>',
         AuthorDetail.as_view(template_name="authors/detail.html"), name='author_detail'),
    path('authors/update/<int:pk>',
         AuthorUpdate.as_view(template_name="authors/update.html"), name='author_update'),
    path('authors/delete/<int:pk>',
         AuthorDelete.as_view(template_name="authors/delete.html"), name='author_delete'),
    path('editorials/', EditorialList.as_view(template_name="editorials/index.html"),
         name='editorial_list'),
    path('editorials/create', EditorialCreate.as_view(template_name="editorials/create.html"),
         name='editorial_create'),
    path('editorials/detail/<int:pk>',
         EditorialDetail.as_view(template_name="editorials/detail.html"), name='editorial_detail'),
    path('editorials/update/<int:pk>',
         EditorialUpdate.as_view(template_name="editorials/update.html"), name='editorial_update'),
    path('editorials/delete/<int:pk>',
         EditorialDelete.as_view(template_name="editorials/delete.html"), name='editorial_delete'),
    path('books/', BookList.as_view(template_name="books/index.html"),
         name='book_list'),
    path('books/create',
         BookCreate.as_view(template_name="books/create.html"), name='book_create'),
    path('books/detail/<int:pk>',
         BookDetail.as_view(template_name="books/detail.html"), name='book_detail'),
    path('books/update/<int:pk>',
         BookUpdate.as_view(template_name="books/update.html"), name='book_update'),
    path('books/delete/<int:pk>',
         BookDelete.as_view(template_name="books/delete.html"), name='book_delete'),
]
