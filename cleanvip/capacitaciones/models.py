from django.db import models

# Create your models here.

class Capacitacion(models.Model):
    nombreCapacitacion = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.IntegerField()
    organizador = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombreCapacitacion