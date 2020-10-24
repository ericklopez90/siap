from model_utils.models import TimeStampedModel
from django.db import models
from applications.controlasist.models import Faltas

# Create your models here.

class Dias(TimeStampedModel):
    nombre = models.CharField('Dias Laborales', max_length=25)

    class Meta:
        verbose_name = 'Dia Laboral'
        verbose_name_plural = 'Dias Laborales'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class CodigoPuesto(TimeStampedModel):
    nombre = models.CharField('Codigo de Puesto', max_length=25)

    class Meta:
        verbose_name = 'Codigo de Puesto'
        verbose_name_plural = 'Codigos de Puestos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class NivelSalarial(TimeStampedModel):
    nivel = models.IntegerField('Nivel Salarial',)

    class Meta:
        verbose_name = 'Nivel Salarial'
        verbose_name_plural = 'Niveles Salariales'
        ordering = ['nivel']

    def __str__(self):
        return str(self.nivel)


class Prestaciones(TimeStampedModel):
    nombre = models.CharField('Prestanción', max_length=35)
    num_dias = models.IntegerField('Dias',)

    class Meta:
        verbose_name = 'Prestacion'
        verbose_name_plural = 'Prestaciones'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class SeccionSindical(TimeStampedModel):
    nombre = models.CharField('Prestanción', max_length=35)
    seccion = models.IntegerField('Dias',)

    class Meta:
        verbose_name = 'Seccion Sindical'
        verbose_name_plural = 'Secciones Sindicales'
        ordering = ['seccion']

    def __str__(self):
        return "sección{self.seccion} - {self.nombre}"


class Universo(TimeStampedModel):
    nombre = models.CharField('Universo', max_length=10)

    class Meta:
        verbose_name = 'Universo'
        verbose_name_plural = 'Universos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class ZonaPagadora(TimeStampedModel):
    nombre = models.CharField('Universo', max_length=10)

    class Meta:
        verbose_name = 'Zona Pagadora'
        verbose_name_plural = 'Zonas Pagadoras'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class TipoContratacion(TimeStampedModel):
    nombre = models.CharField('Tipo de contratación', max_length=100)

    class Meta:
        verbose_name = 'Tipo de Contratación'
        verbose_name_plural = 'Tipos de Contratación'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class Turno(TimeStampedModel):
    nombre = models.CharField('Turno', max_length=15)
    dia_trab = models.ManyToManyField(Dias)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['id']

    def __str__(self):
        return str(self.id)


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

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'
        ordering = ['apellido_paterno']
        unique_together = ['num_empleado']

    def __str__(self):
        return "{self.num_plaza}-{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
        #return str(self.num_plaza) + ' - ' + self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
     