from model_utils.models import TimeStampedModel
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faltas(TimeStampedModel):
    fecha = models.DateField('Fecha',) 
    falta = models.BooleanField('Falta', default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Falta'
        verbose_name_plural = 'Faltas'
        

    def __str__(self):
        return str(self.id)
