# contrataciones/forms.py

from django import forms
from .models import Contratacion

class ContratacionForm(forms.ModelForm):
    class Meta:
        model = Contratacion
        fields = ['colaborador', 'fecha_contratacion', 'posicion', 'salario_inicial', 'duracion_contrato']
