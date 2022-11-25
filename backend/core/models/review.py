from django.db import models
from .book import Book
from .user import User

class Review(models.Model):
    user = models.ForeignKey(User, related_name="review", on_delete=models.CASCADE, null=False, default=None)
    book = models.ForeignKey(Book, related_name="review", on_delete=models.CASCADE, null=False, default=None)
    comment = models.CharField(max_length=2000, null=True)
    stars = models.FloatField(null=False)

    def __str__(self) :
        return self.book.name_book