from model_utils.models import TimeStampedModel
from django.db import models

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