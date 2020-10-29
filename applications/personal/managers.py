# python
from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F


class PersonalManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_personal(self, kword, order):
        consulta = self.filter(
            Q (nombre__icontains=kword) | Q (num_empleado__icontains=kword)
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