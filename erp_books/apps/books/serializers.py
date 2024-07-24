from rest_framework import serializers
from .models import Editorial, Author, Book


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        # fields = "__all__"
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = "__all__"
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = "__all__"
        fields = ['title', 'page', 'edition_date', 'editorial', 'author']
