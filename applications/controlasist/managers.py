# python
from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F


class FaltasManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_faltas(self, kword, order):
        consulta = self.filter(
            Q (nombre__icontains=kword) | 
            Q (apellido_paterno__icontains=kword) | 
            Q (apellido_materno__icontains=kword) | 
            Q (num_empleado=kword) |
            Q (num_plaza=kword)
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

    def buscar_faltaspersonal(self, pk):
        return self.filter(
            personal__id=pk
        ).order_by('-created')
