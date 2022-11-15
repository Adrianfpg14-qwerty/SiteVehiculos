from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from Apps.multas.models import Multa
from Apps.multas.serializers import MultaSerializer

# Create your views here.


class MultaList(APIView):
    """
    Lista de Multas
    """

    def get(self, request, format=None):
        multas = Multa.objects.all()
        serializer = MultaSerializer(multas, many=True)
        return Response({"multas":serializer.data})

    def post(self, request, format=None):
        serializer = MultaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MultaDetail(APIView):
    """
    Retrieve, update or delete de los multas por pk
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Multa.objects.get(pk=pk)
        except Multa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        multa = self.get_object(pk)
        serializer = MultaSerializer(multa)
        return Response({"multa":serializer.data})

    def put(self, request, pk, format=None):
        multa = self.get_object(pk)
        serializer = MultaSerializer(multa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        multa = self.get_object(pk)
        serializer = MultaSerializer(multa,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        multa = self.get_object(pk)
        multa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
