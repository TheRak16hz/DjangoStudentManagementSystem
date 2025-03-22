# Generated by Django 4.1.13 on 2024-09-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trayecto_cursante', models.CharField(choices=[('Trayecto 1', 'Trayecto 1'), ('Trayecto 2', 'Trayecto 2'), ('Trayecto 3', 'Trayecto 3'), ('Trayecto 4', 'Trayecto 4')], max_length=255)),
                ('docente_metodologico', models.CharField(max_length=255)),
                ('docente_academico', models.CharField(max_length=255)),
                ('estudiantes', models.CharField(max_length=500)),
            ],
        ),
    ]
