# Generated by Django 5.1 on 2024-10-24 01:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_rename_autor_foro_creador_alter_foro_titulo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('foro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='App.foro')),
            ],
        ),
    ]
