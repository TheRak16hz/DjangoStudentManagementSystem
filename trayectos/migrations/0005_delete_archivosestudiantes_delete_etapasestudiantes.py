# Generated by Django 4.1.13 on 2024-11-21 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trayectos', '0004_trayectos_all'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArchivosEstudiantes',
        ),
        migrations.DeleteModel(
            name='EtapasEstudiantes',
        ),
    ]
