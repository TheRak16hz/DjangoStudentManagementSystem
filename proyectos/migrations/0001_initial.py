# Generated by Django 4.1.13 on 2024-11-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivosEstudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_archivos', models.CharField(max_length=10)),
                ('Proyecto', models.FileField(upload_to='proyectos/')),
                ('Capitulos', models.FileField(upload_to='capitulos/')),
                ('Grupo_est_id', models.CharField(max_length=50)),
            ],
        ),
    ]
