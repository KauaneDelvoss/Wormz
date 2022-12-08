from django.db import models
from .answer import Answer
from .genre import Genre
#from .resolves import Resolves

class Question(models.Model) :
    text = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre, related_name="genres")
    # answer = models.ManyToManyField(Answer,related_name="answer_question", null=True)
  #  answer = models.ManyToManyField(Resolves,related_name="answer_question")

    


    def __str__(self) :
        return self.text
    class Meta:
        verbose_name_plural = "Questions"