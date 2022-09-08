from email.policy import default
from django.db import models

# Create your models here.

class User(models.Model):
    # codadress
    # codbookshelf
    # name_user = models.CharField(max_length=100)  # not null
    cod_user = models.IntegerField(default=0)
    nickname = models.CharField(max_length=50)  # not null unique
    #password = models.CharField(max_length=15)  # not null -> tem que mudar no modelo
    #email = models.EmailField(max_length=50)  # not null
    #admin = models.BooleanField(default=False)
    #genre_pref = models.CharField(max_length=50, null=True)
    user_biography = models.TextField(max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname
    
    class Meta:
        verbose_name_plural = "Users"

    # FOREIGN KEY(cod_adress) REFERENCES adress (cod_adress),
    # FOREIGN KEY(cod_bookshelf) REFERENCES bookshelf (cod_bookshelf)
