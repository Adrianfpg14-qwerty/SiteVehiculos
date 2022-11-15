from dataclasses import field
from statistics import mode

from rest_framework import serializers
from Apps.vehiculos.models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = "__all__"