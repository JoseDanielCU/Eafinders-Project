from django.db import models

class Amigo(models.Model):
    nombre = models.CharField(max_length=100, default='')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
