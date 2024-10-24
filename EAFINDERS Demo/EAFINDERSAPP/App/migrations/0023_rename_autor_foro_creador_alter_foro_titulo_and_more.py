# Generated by Django 5.1 on 2024-10-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_foro_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foro',
            old_name='autor',
            new_name='creador',
        ),
        migrations.AlterField(
            model_name='foro',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
