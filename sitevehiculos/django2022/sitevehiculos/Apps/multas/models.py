from django.db import models
from django.utils.timezone import now

from Apps.personas.models import Persona

# Create your models here.

class Multa(models.Model):
    consecutivoDeMultas = models.CharField(max_length=100, help_text="Ingrese el Consecutivo de Multa")
    fechaYHora = models.DateField(default=now, verbose_name="Fecha Actual")
    lugarInfracion = models.CharField(max_length=100, help_text="Ingrese el lugar de la Infración")

    # persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    # persona_id = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Persona")
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Persona")
    # persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "multa"
        verbose_name_plural = "multas"
