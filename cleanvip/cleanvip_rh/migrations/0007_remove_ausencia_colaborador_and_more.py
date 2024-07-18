# Generated by Django 5.0.6 on 2024-07-18 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanvip_rh', '0006_categoria_newscategory_newspost_postcomment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ausencia',
            name='colaborador',
        ),
        migrations.RemoveField(
            model_name='bonificacion',
            name='colaborador',
        ),
        migrations.RemoveField(
            model_name='bonificacion',
            name='evaluacion',
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='capacitacion',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='departamento',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='colaborador',
        ),
        migrations.RemoveField(
            model_name='departamentos',
            name='jefe_departamento',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='colaborador',
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='colaborador',
        ),
        migrations.RemoveField(
            model_name='evaluacion',
            name='contrato',
        ),
        migrations.RemoveField(
            model_name='datoindicador',
            name='indicador',
        ),
        migrations.RemoveField(
            model_name='seguimientometa',
            name='meta',
        ),
        migrations.DeleteModel(
            name='Ausencia',
        ),
        migrations.DeleteModel(
            name='Bonificacion',
        ),
        migrations.DeleteModel(
            name='Capacitacion',
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.DeleteModel(
            name='Departamentos',
        ),
        migrations.DeleteModel(
            name='Colaborador',
        ),
        migrations.DeleteModel(
            name='Inscripcion',
        ),
        migrations.DeleteModel(
            name='Contrato',
        ),
        migrations.DeleteModel(
            name='Evaluacion',
        ),
        migrations.DeleteModel(
            name='DatoIndicador',
        ),
        migrations.DeleteModel(
            name='Indicador',
        ),
        migrations.DeleteModel(
            name='Meta',
        ),
        migrations.DeleteModel(
            name='SeguimientoMeta',
        ),
    ]
