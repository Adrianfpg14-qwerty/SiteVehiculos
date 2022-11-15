from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from Apps.vehiculos.models import Vehiculo
from Apps.vehiculos.serializers import VehiculoSerializer

# Create your views here.


class VehiculoList(APIView):
    """
    Lista de Vehiculos
    """

    def get(self, request, format=None):
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response({"vehiculos":serializer.data})

    def post(self, request, format=None):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehiculoDetail(APIView):
    """
    Retrieve, update or delete de los vehiculos por pk
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vehiculo = self.get_object(pk)
        serializer = VehiculoSerializer(vehiculo)
        return Response({"vehiculo":serializer.data})

    def put(self, request, pk, format=None):
        vehiculo = self.get_object(pk)
        serializer = VehiculoSerializer(vehiculo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        vehiculo = self.get_object(pk)
        serializer = VehiculoSerializer(vehiculo,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        vehiculo = self.get_object(pk)
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
