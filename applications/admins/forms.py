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
    Dias,
    Hospital,
    PrestacionIndi
)

#Forms
class DiasForm(forms.ModelForm):
    class Meta:
        model = Dias
        fields = (
            'id',
            'nombre',
            'activo',
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        )
    }

class CodigoPuestoForm(forms.ModelForm):
    class Meta:
        model = CodigoPuesto
        fields = (
            'id',
            'nombre',
            'activo',
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        )
    }


class NivelSalarialForm(forms.ModelForm):
    class Meta:
        model = NivelSalarial
        fields = (
            'id',
            'nivel',
            'activo',
        )
        widgets = {
        'nivel': forms.TextInput(
            attrs={
                'placeholder': 'Nivel',
                'class': 'form-control'
            }
        )
    }


class SeccionSindicalForm(forms.ModelForm):
    class Meta:
        model = SeccionSindical
        fields = (
            'id',
            'nombre',
            'seccion',
            'activo',
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        ),
        'seccion': forms.NumberInput(
            attrs={
                'placeholder': 'Seccion',
                'class': 'form-control'
            }
        )
    }


class UniversoForm(forms.ModelForm):
    class Meta:
        model = Universo
        fields = (
            'id',
            'nombre',
            'activo',
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
        fields = (
            'id',
            'nombre',
            'activo',
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        )
    }

class TipoContratacionForm(forms.ModelForm):
    class Meta:
        model = TipoContratacion
        fields = (
            'id',
            'nombre',
            'activo',
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        )
    }


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = (
            'id',
            'nombre',
            'activo',
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        )
    }



class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = (
            'id',
            'nombre',
            'dia_trab',
            'activo',
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        ),
        'dia_trab': forms.SelectMultiple(
            attrs={
                'placeholder': 'Dia Laboral',
                'class': 'form-control'
            }
        )
    }   


class PrestacionIndiForm(forms.ModelForm):
    class Meta:
        model = PrestacionIndi
        fields = (
            'nombre',
            'num_dias',
            'activo'
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        ),
        'num_dias': forms.NumberInput(
            attrs={
                'placeholder': 'Dias Correspondientes',
                'class': 'form-control'
            }
        )
    }


class PrestacionesForm(forms.ModelForm):
    class Meta:
        model = Prestaciones
        fields = (
            'nombre',
            'prestacion',
            'activo',
            'turno',
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        ),
        'prestacion': forms.SelectMultiple(
            attrs={
                'placeholder': 'Prestaciones',
                'class': 'form-control'
            }
        ),
        'turno': forms.Select(
            attrs={
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        )
    }
