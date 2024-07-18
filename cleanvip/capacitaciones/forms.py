# aplicaciones/capacitaciones/forms.py

from django import forms
from .models import Capacitacion

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = '__all__'
