
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
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        ),
        'fecha_nac': forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'Fecha',
                'class': 'input-group-field',
            },
        )
    }