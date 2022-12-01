from django.db import models


class Answer(models.Model) :
    status = models.IntegerField(null=False)
    text = models.CharField(max_length=500)
    

    def __str__(self) :
        return self.text

    class Meta:
        verbose_name_plural = "Answers"