# Generated by Django 5.1 on 2024-10-24 02:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0027_comentario_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='foro',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='foros_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
