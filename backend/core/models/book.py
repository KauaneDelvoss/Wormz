
from django.db import models
from .author import Author
from .genre import Genre

class Book(models.Model):
    resume = models.CharField(max_length=2000, null=True)
    name_book = models.CharField(max_length=100)
    #cod_book = models.AutoField(primary_key=True) #mudou de integerfield para autoincrement
    #year = models.YearField(null=True)
    pages = models.IntegerField(null=True)
    author = models.ManyToManyField(Author, related_name="author_books")
    genre = models.ManyToManyField(Genre, related_name="genre_books")

    def __str__(self) :
        return self.name_book

    class Meta:
        verbose_name_plural = "Books"