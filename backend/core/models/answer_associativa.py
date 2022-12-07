
from django.db import models
from .user import User
from.answer import Answer
from .question import Question

class AnswerAssociativa(models.Model) :
    cod_resp_forms = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    cod_answer = models.ForeignKey(Answer, on_delete=models.PROTECT, null=False, blank=False)
    cod_question = models.ForeignKey(Question,on_delete=models.PROTECT, null=False, blank=False) 
    
    def __str__(self) :
        return "Formulario"

    class Meta:
        verbose_name_plural = "AnswerAssociativa"