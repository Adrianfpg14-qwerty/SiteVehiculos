from dataclasses import field
from statistics import mode

from rest_framework import serializers
from Apps.multas.models import Multa

class MultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multa
        fields = "__all__"