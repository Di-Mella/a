# contrataciones/models.py

from django.db import models
from colaboradores.models import Colaborador

class Contratacion(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='contrataciones')
    fecha_contratacion = models.DateField()
    posicion = models.CharField(max_length=255)
    salario_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_contrato = models.CharField(max_length=255)  # por ejemplo, "6 meses", "1 año", etc.

    def __str__(self):
        return f"Contratación de {self.colaborador.nombre} el {self.fecha_contratacion}"
