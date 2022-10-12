from django.db import models
from core.models import Book, Genre

class Type(models.Model):
    cod_book = models.ForeignKey(Book, on_delete=models.PROTECT)
    cood_genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

    def __str__(self) :
        return f"{self.cod_book}, {self.cood_genre}"

    class Meta:
        verbose_name_plural = "Type"