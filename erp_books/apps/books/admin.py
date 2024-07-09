from django.contrib import admin

# Register your models here.
from .models import Editorial, Author, Book

admin.site.register(Book)
admin.site.register(Editorial)
admin.site.register(Author)
