from model_utils.models import TimeStampedModel
from django.db import models
from applications.admins.models import *
from .managers import PersonalManager

# Create your models here.


class Personal(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=50)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=25)
    apellido_materno = models.CharField('Apellido Materno', max_length=25)
    fecha_nac = models.DateField('Fecha de Nacimiento')
    curp = models.CharField('C.U.R.P.', max_length=18)
    rfc = models.CharField('R.F.C.', max_length=13)
    num_empleado = models.CharField('N° Empleado', max_length=20, unique=True)
    num_plaza = models.CharField('N° Plaza', max_length=20)
    fecha_ingreso = models.DateField('Fecha de Ingreso',)
    universo = models.ForeignKey(Universo, on_delete=models.PROTECT)
    nivel = models.ForeignKey(NivelSalarial, on_delete=models.PROTECT)
    zona_pagadora = models.ForeignKey(ZonaPagadora, on_delete=models.PROTECT)
    codigo_puesto = models.ForeignKey(CodigoPuesto, on_delete=models.PROTECT)
    secc_sindical = models.ForeignKey(SeccionSindical, on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    prestaciones = models.ForeignKey(Prestaciones, on_delete=models.PROTECT)
    tipo_contratacion = models.ForeignKey(TipoContratacion, on_delete=models.PROTECT)
    activo = models.BooleanField('Activo', default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    objects = PersonalManager()

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'
        ordering = ['apellido_paterno']
        unique_together = ['num_empleado']

    def __str__(self):
        return str(self.num_empleado) + ' - ' + self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
     