# Generated by Django 5.1 on 2024-10-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0032_alter_etiqueta_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etiqueta',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]