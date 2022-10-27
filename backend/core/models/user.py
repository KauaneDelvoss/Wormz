from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
   
    #cod_user = models.AutoField(primary_key=True, default=None)
    username = models.CharField(max_length=50, unique=True)  
    email = models.EmailField(max_length=50)  
    genre_pref = models.CharField(max_length=50)
    user_biography = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #name_user = models.CharField(max_length=100)
    #password = models.IntegerField()  # not null é o default -> tem que mudar no modelo
    #admin = models.BooleanField(default=False)

    #cod_adress = models.ForeignKey('Adress', on_delete=models.PROTECT)
    # cod_bookshelf = models.ForeignKey(Bookshelf, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = "Users"