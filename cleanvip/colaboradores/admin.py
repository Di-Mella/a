from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id_genero', 'genero')
    search_fields = ('genero',)

@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ('id_departamento', 'nombre')
    search_fields = ('nombre',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id_cargo', 'nombre', 'departamento')
    search_fields = ('nombre', 'departamento__nombre')
    list_filter = ('departamento',)

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('id_estado_civil', 'estado')
    search_fields = ('estado',)

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'departamento', 'cargo', 'estado_civil')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'rut', 'departamento__nombre', 'cargo__nombre', 'estado_civil__estado')
    list_filter = ('departamento', 'cargo', 'estado_civil', 'id_genero')