# Generated by Django 5.1 on 2024-09-27 23:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_usuario_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigos_de', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
