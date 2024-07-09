import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Editorial(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.num_books()})"

    def num_books(self):
        return self.books.count()


class Book(models.Model):
    title = models.CharField(max_length=20)
    page = models.IntegerField(default=0)
    edition_date = models.DateField("date published")
    editorial = models.ForeignKey(
        Editorial, on_delete=models.CASCADE, null=False, related_name="books", blank=False)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=False, related_name="books", blank=False)

    def __str__(self):
        return f"{self.title} ({self.page})"

    def was_published_recently(self):
        return self.edition_date >= timezone.now() - datetime.timedelta(days=1)
