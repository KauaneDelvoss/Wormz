from django.db import models


class Author(models.Model) :
    name_author = models.CharField(max_length=100)
    author_biography = models.CharField(max_length=2000)
    #cod_author = models.IntegerField(primary_key = True)
    #book = models.ManyToManyField('book.Book')

    def __str__(self) :
        return self.name_author

    class Meta:
        verbose_name_plural = "Authors"