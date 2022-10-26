
from django.db import models

class Genre(models.Model) :
    name_genre = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    cod_genre = models.AutoField(primary_key=True)

    def __str__(self) :
        return self.name_genre

    class Meta:
        verbose_name_plural = "Genres"