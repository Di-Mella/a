# bonificaciones/forms.py

from django import forms
from .models import Evaluacion, Bonificacion

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['colaborador', 'fecha_evaluacion', 'puntaje', 'comentarios']

class BonificacionForm(forms.ModelForm):
    class Meta:
        model = Bonificacion
        fields = ['colaborador', 'evaluacion', 'monto', 'fecha_bonificacion']
