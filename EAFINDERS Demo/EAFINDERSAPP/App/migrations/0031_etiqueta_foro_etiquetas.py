# Generated by Django 5.1 on 2024-10-24 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0030_comentario_archivo_alter_foro_foto_foro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='foro',
            name='etiquetas',
            field=models.ManyToManyField(blank=True, related_name='foros', to='App.etiqueta'),
        ),
    ]
