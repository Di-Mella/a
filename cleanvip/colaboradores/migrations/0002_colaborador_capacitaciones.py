# Generated by Django 5.0.6 on 2024-07-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacitaciones', '0001_initial'),
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='capacitaciones',
            field=models.ManyToManyField(related_name='colaboradores', to='capacitaciones.capacitacion'),
        ),
    ]
