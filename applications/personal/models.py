from model_utils.models import TimeStampedModel
from django.db import models
from applications.controlasist.models import Faltas
from applications.admins.models import *

# Create your models here.


class Personal(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=50)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=25)
    apellido_materno = models.CharField('Apellido Materno', max_length=25)
    fecha_nac = models.DateField('Fecha de Nacimiento')
    curp = models.CharField('C.U.R.P.', max_length=18)
    rfc = models.CharField('R.F.C.', max_length=13)
    num_empleado = models.IntegerField('N° Empleado', unique=True)
    num_plaza = models.IntegerField('N° Plaza',)
    fecha_ingreso = models.DateField('Fecha de Ingreso',)
    universo = models.ForeignKey(Universo, on_delete=models.CASCADE)
    nivel = models.ForeignKey(NivelSalarial, on_delete=models.CASCADE)
    zona_pagadora = models.ForeignKey(ZonaPagadora, on_delete=models.CASCADE)
    codigo_puesto = models.ForeignKey(CodigoPuesto, on_delete=models.CASCADE)
    secc_sindical = models.ForeignKey(SeccionSindical, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    prestaciones = models.ForeignKey(Prestaciones, on_delete=models.CASCADE)
    faltas = models.ForeignKey(Faltas, on_delete=models.CASCADE, related_name='faltas_personal')
    tipo_contratacion = models.ForeignKey(TipoContratacion, on_delete=models.CASCADE)
    active = models.BooleanField('Activo', default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'
        ordering = ['apellido_paterno']
        unique_together = ['num_empleado']

    def __str__(self):
        return "{self.num_plaza}-{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
        #return str(self.num_plaza) + ' - ' + self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
     