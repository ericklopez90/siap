# python
from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F


class DiasManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_dias(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('created')

class CodigoPuestoManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_codigopuesto(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')

class NivelSalarialManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_nivelsalarial(self, kword, order):
        consulta = self.filter(
            nivel__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nivel':
            # ordenar por fecha
            return consulta.order_by('nivel')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')


class SeccionSindicalManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_seccionsindical(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')


class UniversoManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_universo(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')


class ZonaPagadoraManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_zonapagadora(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')


class TipoContratacionManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_tipocontratacion(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')


class HospitalManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_hospital(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')


class TurnoManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_turno(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')


class PrestacionIndiManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_prestacionindi(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')



class PrestacionesManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_prestaciones(self, kword, order):
        consulta = self.filter(
            nombre__icontains=kword
        )
        # verificamos en que orden se solicita
        if order == 'nombre':
            # ordenar por fecha
            return consulta.order_by('nombre')
        elif order == 'modified':
            # ordenar por nombre
            return consulta.order_by('modified')
        elif order == 'user':
            return consulta.order_by('user')
        else:
            return consulta.order_by('-created')
