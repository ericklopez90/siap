from django.contrib import admin
from .models import (
    Personal,
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

admin.site.register(Personal)