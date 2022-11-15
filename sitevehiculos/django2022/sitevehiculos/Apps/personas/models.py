from django.db import models

# Create your models here.


class Persona(models.Model):
    dni = models.IntegerField(verbose_name="DNI")
    # dni = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="DNI")
    nombre = models.CharField(max_length=100, help_text="Ingrese el Nombre de la Persona")
    apellidos = models.CharField(max_length=100, help_text="Ingrese el Apellido de la Persona")
    direccion = models.CharField(max_length=100, help_text="Ingrese la Direccion de la Persona")
    telefono = models.CharField(max_length=12, help_text="Ingrese el Telefono de la Persona")
    ciudad = models.CharField(max_length=100, help_text="Ingrese la ciudad de la Persona")
    tipoDePersonas = models.CharField(max_length=100, help_text="Ingrese el Tipo de Persona (Natural/Juridica)")

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"
