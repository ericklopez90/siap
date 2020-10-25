from django.contrib import admin

from .models import (
    Prestaciones, 
    Turno, 
    TipoContratacion, 
    Universo, 
    ZonaPagadora, 
    SeccionSindical,
    NivelSalarial,
    CodigoPuesto,
    Dias
)
# Register your models here.

admin.site.register(Prestaciones)

admin.site.register(Turno)

admin.site.register(TipoContratacion)

admin.site.register(Universo)

admin.site.register(ZonaPagadora)

admin.site.register(SeccionSindical)

admin.site.register(NivelSalarial)

admin.site.register(CodigoPuesto)

admin.site.register(Dias)