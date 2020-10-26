from django import forms
#local
from .models import (
    Universo,
    ZonaPagadora,
    SeccionSindical,
    Prestaciones,
    TipoContratacion,
    NivelSalarial,
    CodigoPuesto,
    Turno,
    Dias
)

#Forms
class UniversoForm(forms.ModelForm):
    class Meta:
        model = Universo
        fields = (
            'nombre',
            'user'
        )
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'class': 'form-control'
                }
            )
        }


class ZonaPagadoraForm(forms.ModelForm):
    class Meta:
        model = ZonaPagadora
        fields = ('__all__')
        

class SeccionSindicalForm(forms.ModelForm):
    class Meta:
        model = SeccionSindical
        fields = ('__all__')


class PrestacionesForm(forms.ModelForm):
    class Meta:
        model = Prestaciones
        fields = ('__all__')


class TipoContratacionForm(forms.ModelForm):
    class Meta:
        model = TipoContratacion
        fields = ('__all__')


class NivelSalarialForm(forms.ModelForm):
    class Meta:
        model = NivelSalarial
        fields = ('__all__')


class CodigoPuestoForm(forms.ModelForm):
    class Meta:
        model = CodigoPuesto
        fields = ('__all__')


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ('__all__')


class DiasForm(forms.ModelForm):
    class Meta:
        model = Dias
        fields = ('__all__')

