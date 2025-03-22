# Generated by Django 4.1.13 on 2024-11-26 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_estudiante_ultimo_año_cursado'),
        ('trayectos', '0005_delete_archivosestudiantes_delete_etapasestudiantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trayecto_egresados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci_est', models.CharField(max_length=10)),
                ('name_est', models.CharField(max_length=32)),
                ('seccion', models.CharField(max_length=10)),
                ('codigo_año', models.CharField(max_length=10)),
                ('ref_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.estudiante')),
            ],
            options={
                'db_table': 'egresados_trayecto',
            },
        ),
        migrations.CreateModel(
            name='Trayecto_inicial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci_est', models.CharField(max_length=10)),
                ('name_est', models.CharField(max_length=32)),
                ('seccion', models.CharField(max_length=10)),
                ('codigo_año', models.CharField(max_length=10)),
                ('ref_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.estudiante')),
            ],
            options={
                'db_table': 'trayecto_inicial',
            },
        ),
        migrations.RemoveField(
            model_name='trayecto2',
            name='ref_cedula',
        ),
        migrations.RemoveField(
            model_name='trayecto3',
            name='ref_cedula',
        ),
        migrations.RemoveField(
            model_name='trayecto4',
            name='ref_cedula',
        ),
        migrations.DeleteModel(
            name='Trayecto1',
        ),
        migrations.DeleteModel(
            name='Trayecto2',
        ),
        migrations.DeleteModel(
            name='Trayecto3',
        ),
        migrations.DeleteModel(
            name='Trayecto4',
        ),
    ]
