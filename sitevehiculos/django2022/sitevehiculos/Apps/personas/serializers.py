from dataclasses import field
from statistics import mode

from rest_framework import serializers
from Apps.personas.models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"