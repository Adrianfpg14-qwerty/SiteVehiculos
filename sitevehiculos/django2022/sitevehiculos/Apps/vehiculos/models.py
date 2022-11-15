from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=100, help_text="Matricula")
    marca = models.CharField(max_length=100, help_text="Marca")
    modelos = models.CharField(max_length=100, help_text="Modelo")

    class Meta:
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"
