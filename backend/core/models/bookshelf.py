from django.db import models
from .book import Book
from .user import User

class Bookshelf(models.Model) :
    bookshelf_name = models.CharField(max_length=100)
    booshelf_desc = models.CharField(max_length=500, null=True)
    #cod_bookshelf = models.AutoField(primary_key = True)
    #cod_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    book = models.ManyToManyField(Book, related_name="bookshelf")
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self) :
        return self.bookshelf_name

    class Meta:
        verbose_name_plural = "Bookshelf"