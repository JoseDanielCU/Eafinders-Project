# Generated by Django 5.0.7 on 2024-09-12 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendsapp', '0006_alter_person_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
    ]