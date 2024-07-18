# Generated by Django 5.0.6 on 2024-07-18 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaboradores', '0002_colaborador_capacitaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contratacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_contratacion', models.DateField()),
                ('posicion', models.CharField(max_length=255)),
                ('salario_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duracion_contrato', models.CharField(max_length=255)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contrataciones', to='colaboradores.colaborador')),
            ],
        ),
    ]