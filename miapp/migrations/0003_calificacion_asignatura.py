# Generated by Django 4.2.13 on 2024-08-04 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_calificacion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='asignatura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='miapp.asignatura'),
        ),
    ]
