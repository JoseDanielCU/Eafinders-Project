from django.db import models

# Create your models here.
class UserRecords(models.Model):
    username = models.CharField(max_length=50)
    description = models.CharField(max_length=300)