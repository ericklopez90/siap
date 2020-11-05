
from django import forms
#local
from .models import Faltas


class FaltasForm(forms.ModelForm):
    class Meta:
        model = Faltas
        fields = (
            'id',
            'fecha',
            'falta'
        )
        widgets = {
        'fecha': forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control',
            },
        ),
        'falta': forms.CheckboxInput(
            attrs={
            },
        ),
    }