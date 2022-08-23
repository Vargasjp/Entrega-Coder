from django.db import models

# Create your models here.

class Familia(models.Model):
    Nombre=models.CharField(max_length=40)
    Apellido=models.CharField(max_length=45)
    Dni=models.IntegerField()
    FechaDeNac=models.DateField()