from django.db import models
from .book import Book
from .bookshelf import Bookshelf

class Own(models.Model):
    cod_book = models.ForeignKey(Book, on_delete=models.PROTECT)
    cod_bookshelf = models.ForeignKey(Bookshelf, on_delete=models.PROTECT)

    def __str__(self) :
        return f"{self.cod_book}, {self.cod_bookshelf}"

    class Meta:
        verbose_name_plural = "Own"