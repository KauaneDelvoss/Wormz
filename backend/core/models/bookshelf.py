from django.db import models
from catalog.settings import AUTH_USER_MODEL

class Bookshelf(models.Model) :
    bookshelf_name = models.CharField(max_length=100)
    booshelf_desc = models.CharField(max_length=500, null=True)
    cod_bookshelf = models.AutoField(primary_key = True)
    cod_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) :
        return self.bookshelf_name

    class Meta:
        verbose_name_plural = "Bookshelf"