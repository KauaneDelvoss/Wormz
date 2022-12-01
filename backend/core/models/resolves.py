from django.db import models
from .user import User 
from .form import Form 


class Resolves(models.Model) :
    cod_user = models.ForeignKey(User,  on_delete=models.CASCADE, null=False, blank=False)                       
    cod_forms = models.ForeignKey(Form,  on_delete=models.PROTECT, null=False, blank=False)
    DTH = models.DateTimeField(null=False, blank=True)

    def __str__(self) :
        return str(self.id)

    class Meta:
        verbose_name_plural = "Resolves"