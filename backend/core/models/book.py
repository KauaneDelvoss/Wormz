from django.db import models

class book(models.Model):
    resume = models.CharField(max_length=2000, null=True)
    name_book = models.CharField(max_length=100)
    cod_book = models.AutoField(primary_key=True) #mudou de integerfield para autoincrement
    year = models.YearField(null=True)
