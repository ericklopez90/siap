from model_utils.models import TimeStampedModel
from django.db import models
from django.contrib.auth.models import User
from .managers import (
    UniversoManager,
    CodigoPuestoManager,
    NivelSalarialManager,
    PrestacionesManager,
    SeccionSindicalManager,
    ZonaPagadoraManager,
    TipoContratacionManager,
    TurnoManager,
    DiasManager,
    HospitalManager,
    PrestacionIndiManager
)


# Create your models here.
class Dias(TimeStampedModel):
    nombre = models.CharField('Dias Laborales', max_length=25)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = DiasManager()

    class Meta:
        verbose_name = 'Dia Laboral'
        verbose_name_plural = 'Dias Laborales'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class CodigoPuesto(TimeStampedModel):
    nombre = models.CharField('Codigo de Puesto', max_length=25)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = CodigoPuestoManager()

    class Meta:
        verbose_name = 'Codigo de Puesto'
        verbose_name_plural = 'Codigos de Puestos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class NivelSalarial(TimeStampedModel):
    nivel = models.IntegerField('Nivel Salarial',)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = NivelSalarialManager()

    class Meta:
        verbose_name = 'Nivel Salarial'
        verbose_name_plural = 'Niveles Salariales'
        ordering = ['nivel']

    def __str__(self):
        return str(self.nivel)


class SeccionSindical(TimeStampedModel):
    nombre = models.CharField('Prestanción', max_length=35)
    seccion = models.IntegerField('Dias',)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = SeccionSindicalManager()

    class Meta:
        verbose_name = 'Seccion Sindical'
        verbose_name_plural = 'Secciones Sindicales'
        ordering = ['seccion']

    def __str__(self):
        return str(self.seccion) + " - " + self.nombre


class Universo(TimeStampedModel):
    nombre = models.CharField('Universo', max_length=10, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = UniversoManager()
    
    class Meta:
        verbose_name = 'Universo'
        verbose_name_plural = 'Universos'
        ordering = ['nombre']
        unique_together = ['nombre']

    def __str__(self):
        return self.nombre


class ZonaPagadora(TimeStampedModel):
    nombre = models.CharField('Universo', max_length=10)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = ZonaPagadoraManager()

    class Meta:
        verbose_name = 'Zona Pagadora'
        verbose_name_plural = 'Zonas Pagadoras'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class TipoContratacion(TimeStampedModel):
    nombre = models.CharField('Tipo de contratación', max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = TipoContratacionManager()

    class Meta:
        verbose_name = 'Tipo de Contratación'
        verbose_name_plural = 'Tipos de Contratación'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class Hospital(TimeStampedModel):
    nombre = models.CharField('Hospital', max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = HospitalManager()

    class Meta:
        verbose_name = 'Tipo de Contratación'
        verbose_name_plural = 'Tipos de Contratación'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class Turno(TimeStampedModel):
    nombre = models.CharField('Turno', max_length=15)
    dia_trab = models.ManyToManyField(Dias)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = TurnoManager()

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class PrestacionIndi(TimeStampedModel):
    nombre = models.CharField('Prestanción', max_length=35)
    num_dias = models.IntegerField('Dias',)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = PrestacionIndiManager()

    class Meta:
        verbose_name = 'Prestacion Individual'
        verbose_name_plural = 'Prestaciones Individuales'
        ordering = ['id']

    def __str__(self):
        return self.nombre + " - " + str(self.num_dias)


class Prestaciones(TimeStampedModel):
    nombre = models.CharField('Prestanciónes', max_length=35)
    prestacion = models.ManyToManyField(PrestacionIndi)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    objects = PrestacionesManager()

    class Meta:
        verbose_name = 'Prestacion'
        verbose_name_plural = 'Prestaciones'
        ordering = ['id']

    def __str__(self):
        return str(self.turno)


