from django.contrib import admin

# Register your models here.
from .models import (
    Colaborador,
    Capacitacion,
    Contrato,
    Evaluacion,
    Bonificacion,
    Inscripcion,
    Usuario,
    Permiso,
    Departamentos,
    Cargo,
    Ausencia,
    Meta,
    SeguimientoMeta,
    Indicador,
    DatoIndicador
)

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'rut', 'cargo', 'fecha_ingreso')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'rut')
    list_filter = ('sexo', 'estado_civil', 'comuna', 'cargo', 'fecha_ingreso')

@admin.register(Capacitacion)
class CapacitacionAdmin(admin.ModelAdmin):
    list_display = ('nombreCapacitacion', 'fecha_inicio', 'fecha_fin', 'organizador', 'costo')
    search_fields = ('nombreCapacitacion', 'organizador')
    list_filter = ('fecha_inicio', 'fecha_fin', 'organizador')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'tipo_contrato', 'fecha_inicio', 'fecha_fin', 'sueldo_base', 'jornada_laboral')
    search_fields = ('colaborador__nombre', 'tipo_contrato')
    list_filter = ('tipo_contrato', 'fecha_inicio', 'fecha_fin', 'jornada_laboral')

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'fecha_evaluacion', 'puntaje_atencion_cliente', 'puntaje_cumplimiento_tareas', 'puntaje_proactividad', 'puntaje_trabajo_en_equipo')
    search_fields = ('contrato__colaborador__nombre', 'fecha_evaluacion')
    list_filter = ('fecha_evaluacion', 'puntaje_atencion_cliente', 'puntaje_cumplimiento_tareas', 'puntaje_proactividad', 'puntaje_trabajo_en_equipo')

@admin.register(Bonificacion)
class BonificacionAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'evaluacion', 'puntaje', 'monto', 'fecha_pago')
    search_fields = ('colaborador__nombre', 'evaluacion__contrato__colaborador__nombre')
    list_filter = ('fecha_pago', 'puntaje', 'monto')

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'capacitacion', 'fecha_inscripcion', 'asistencia')
    search_fields = ('colaborador__nombre', 'capacitacion__nombreCapacitacion')
    list_filter = ('fecha_inscripcion', 'asistencia')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'email', 'tipo_usuario')
    search_fields = ('nombre', 'rut', 'email')
    list_filter = ('tipo_usuario',)

@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    filter_horizontal = ('usuario',)

@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'jefe_departamento')
    search_fields = ('nombre', 'jefe_departamento__nombre')
    list_filter = ('jefe_departamento',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'sueldo_minimo', 'sueldo_maximo')
    search_fields = ('nombre', 'departamento__nombre')
    list_filter = ('departamento',)

@admin.register(Ausencia)
class AusenciaAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'tipo_ausencia', 'fecha_inicio', 'fecha_fin')
    search_fields = ('colaborador__nombre', 'tipo_ausencia')
    list_filter = ('tipo_ausencia', 'fecha_inicio', 'fecha_fin')

@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'periodo', 'descripcion', 'indicador_medicion', 'valor_objetivo')
    search_fields = ('colaborador__nombre', 'periodo', 'descripcion')
    list_filter = ('periodo', 'indicador_medicion')

@admin.register(SeguimientoMeta)
class SeguimientoMetaAdmin(admin.ModelAdmin):
    list_display = ('meta', 'fecha_seguimiento', 'valor_alcanzado')
    search_fields = ('meta__colaborador__nombre', 'fecha_seguimiento')
    list_filter = ('fecha_seguimiento',)

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'frecuencia_medicion', 'meta_objetivo')
    search_fields = ('nombre',)
    list_filter = ('frecuencia_medicion',)

@admin.register(DatoIndicador)
class DatoIndicadorAdmin(admin.ModelAdmin):
    list_display = ('indicador', 'periodo', 'valor')
    search_fields = ('indicador__nombre', 'periodo')
    list_filter = ('periodo',)