# Generated by Django 5.1 on 2024-09-27 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email_institucional', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='El correo debe terminar en @eafit.edu.co', regex='^[\\w\\.-]+@eafit\\.edu\\.co$')])),
                ('password', models.CharField(max_length=128)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='perfil_fotos/')),
                ('biografia', models.TextField(blank=True, null=True)),
                ('carrera', models.CharField(blank=True, max_length=100, null=True)),
                ('semestre', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]