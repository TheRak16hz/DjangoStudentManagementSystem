# Generated by Django 4.1.13 on 2024-09-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesores',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
