# Generated by Django 5.1 on 2024-08-31 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendsapp.person')),
            ],
        ),
    ]