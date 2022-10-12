from django.db import models
from .author import Author
from .book import Book

class Writes(models.Model) :
    cod_book = models.ForeignKey(Book, on_delete=models.PROTECT)
    cod_author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self) :
        return f"{self.cod_book}, {self.cod_author}"

    class Meta:
        verbose_name_plural = "Writes"