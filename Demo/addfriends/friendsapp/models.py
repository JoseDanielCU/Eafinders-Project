from django.core.exceptions import ValidationError
from django.db import models

def validate_eafit_email(value):
    if not value.endswith('@eafit.edu.co'):
        raise ValidationError('El correo debe terminar en @eafit.edu.co')

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Friend(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)