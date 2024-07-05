from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Departamentos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    jefe_departamento = models.ForeignKey('Colaborador', on_delete=models.SET_NULL, null=True, blank=True, related_name='jefe_departamento')

    def __str__(self):
        return f"{self.nombre}"
class Colaborador(models.Model):
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')))
    estado_civil = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    cargo = models.CharField(max_length=255)
    fecha_ingreso = models.DateField()
    sueldo_base = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.ForeignKey(Departamentos, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
    



class Capacitacion(models.Model):
    nombreCapacitacion = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.IntegerField()
    organizador = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombreCapacitacion} ({self.fecha_inicio} - {self.fecha_fin})"
    
class Contrato(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    tipo_contrato = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    sueldo_base = models.DecimalField(max_digits=10, decimal_places=2)
    jornada_laboral = models.CharField(max_length=255)
    bonificaciones = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Contrato para {self.colaborador.nombre} ({self.tipo_contrato})"
    
class Evaluacion(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    fecha_evaluacion = models.DateField()
    puntaje_atencion_cliente = models.IntegerField()
    puntaje_cumplimiento_tareas = models.IntegerField()
    puntaje_proactividad = models.IntegerField()
    puntaje_trabajo_en_equipo = models.IntegerField()
    comentarios = models.TextField()

    def __str__(self):
        return f"Evaluación para {self.contrato.colaborador.nombre} ({self.fecha_evaluacion})"
    
class Bonificacion(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    def __str__(self):
        return f"Bonificación para {self.colaborador.nombre} ({self.monto})"
    

class Inscripcion(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    capacitacion = models.ForeignKey(Capacitacion, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    asistencia = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.colaborador.nombre} inscrito en {self.capacitacion.nombre}"

class Usuario(AbstractBaseUser, models.Model):
    nombre = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20, choices=(('admin', 'Administrador'), ('rrhh', 'Personal de RRHH')))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'rut', 'tipo_usuario']

    objects = BaseUserManager()

    def __str__(self):
        return f"{self.nombre} ({self.email})"

    def is_staff(self):
        return self.tipo_usuario == 'admin'

    def is_superuser(self):
        return self.tipo_usuario == 'admin'
    
class Permiso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    usuario = models.ManyToManyField(Usuario)

    def __str__(self):
        return f"{self.nombre} ({self.usuario.all()})"
    
class Cargo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    sueldo_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    sueldo_maximo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.departamento.nombre})"
    
class Ausencia(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    tipo_ausencia = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    justificacion = models.TextField()

    def __str__(self):
        return f"{self.colaborador.nombre} - {self.tipo_ausencia} ({self.fecha_inicio} - {self.fecha_fin})"
    
class Meta(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=255)  # Ejemplo: "2023-07-01 - 2023-12-31"
    descripcion = models.TextField()
    indicador_medicion = models.CharField(max_length=255)
    valor_objetivo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.colaborador.nombre} - {self.descripcion} ({self.periodo})"

class SeguimientoMeta(models.Model):
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)
    fecha_seguimiento = models.DateField()
    valor_alcanzado = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField()

    def __str__(self):
        return f"{self.meta.descripcion} - Seguimiento ({self.fecha_seguimiento})"
    
class Indicador(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    formula_calculo = models.TextField()  # Opcional, si se calcula automáticamente
    frecuencia_medicion = models.CharField(max_length=255, choices=(('mensual', 'Mensual'), ('trimestral', 'Trimestral'), ('anual', 'Anual')))
    meta_objetivo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.frecuencia_medicion})"

class DatoIndicador(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=255)  # Ejemplo: "2023-07-01 - 2023-12-31"
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.indicador.nombre} - {self.periodo}: {self.valor}"