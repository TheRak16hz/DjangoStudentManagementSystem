# Generated by Django 4.1.13 on 2024-09-20 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_estudiante_status'),
        ('trayectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trayecto1',
            name='ref_cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.estudiante'),
        ),
        migrations.AlterField(
            model_name='trayecto2',
            name='ref_cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.estudiante'),
        ),
        migrations.AlterField(
            model_name='trayecto3',
            name='ref_cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.estudiante'),
        ),
        migrations.AlterField(
            model_name='trayecto4',
            name='ref_cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.estudiante'),
        ),
    ]
