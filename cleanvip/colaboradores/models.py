from django.db import models
from capacitaciones.models import Capacitacion
# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)
    
class Departamentos(models.Model):
    id_departamento = models.AutoField(db_column='idDepartamento', primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField()
    jefe_departamento = models.ForeignKey('Colaborador', on_delete=models.SET_NULL, null=True, blank=True, related_name='jefe_departamento')
    def __str__(self):
        return str(self.nombre)
    

class Cargo(models.Model):
    id_cargo = models.AutoField(db_column='idCargo', primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class EstadoCivil(models.Model):
    id_estado_civil = models.AutoField(db_column='idEstadoCivil', primary_key=True)
    estado = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.estado)


class Colaborador(models.Model):
    rut = models.CharField(max_length=12, unique=True, primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, db_column='idEstadoCivil')
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, db_column='idCargo')
    fecha_ingreso = models.DateField()
    sueldo_base = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE, db_column='idDepartamento')
    capacitaciones = models.ManyToManyField(Capacitacion, related_name='colaboradores')
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"


