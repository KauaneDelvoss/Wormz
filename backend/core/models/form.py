
from django.db import models
from .user import User
from .question import Question

class Form(models.Model) :
    name_forms = models.IntegerField(null=True)
    cod_user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    # genre = models.ManyToManyField(Genre, related_name="genre_books")
    #user = models.ManyToManyField(User, related_name="resolve")
    question = models.ManyToManyField(Question, related_name="form_question")
    
    def __str__(self) :
        return str(self.name_forms)

    class Meta:
        verbose_name_plural = "Forms"