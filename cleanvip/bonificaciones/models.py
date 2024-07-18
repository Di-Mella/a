# bonificaciones/models.py

from django.db import models
from colaboradores.models import Colaborador

class Evaluacion(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='evaluaciones')
    fecha_evaluacion = models.DateField()
    puntaje = models.IntegerField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Evaluación de {self.colaborador.nombre} el {self.fecha_evaluacion}"

class Bonificacion(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='bonificaciones')
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='bonificaciones')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_bonificacion = models.DateField()

    def __str__(self):
        return f"Bonificación de {self.colaborador.nombre} el {self.fecha_bonificacion}"
