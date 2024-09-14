# Generated by Django 5.0.7 on 2024-09-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendsapp', '0002_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='confirm_password',
            field=models.CharField(default=12345, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=12345, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=12345, max_length=100),
            preserve_default=False,
        ),
    ]
