# Generated by Django 5.0.7 on 2024-09-12 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendsapp', '0004_remove_person_confirm_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='confirm_passwod',
            new_name='confirm_password',
        ),
    ]
