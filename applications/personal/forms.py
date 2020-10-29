
from django import forms
#local
from .models import Personal


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = (
            'id',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nac',
            'curp',
            'rfc',
            'num_empleado',
            'num_plaza',
            'fecha_ingreso',
            'universo',
            'nivel',
            'zona_pagadora',
            'codigo_puesto',
            'secc_sindical',
            'hospital',
            'turno',
            'prestaciones',
            'tipo_contratacion',
            'activo'
        )
        widgets = {
        'nombre': forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),
        'apellido_paterno': forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),
        'apellido_materno': forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),
        'fecha_nac': forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control',
            },
        ),
        'curp': forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),
        'rfc': forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),
        'num_empleado': forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),
        'num_plaza': forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),
        'fecha_ingreso': forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
        ),
        'universo': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'nivel': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'zona_pagadora': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'codigo_puesto': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'secc_sindical': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'hospital': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'turno': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'prestaciones': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'tipo_contratacion': forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        'activo': forms.CheckboxInput(
            attrs={
            },
        ),
    }