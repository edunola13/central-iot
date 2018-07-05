# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from sensors.models import Sensor, SensorReading
from sensors.serializers import SensorSerializer, SensorDetailSerializer, SensorReadingSerializer, SensorReadingDetailSerializer
from RobotApiRest.permissions import AutomatizadorOrReadOnly


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = (IsAuthenticated, AutomatizadorOrReadOnly, )
    #Este va cuando es distinto al definido en la configuracion
    #filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    __basic_fields = ('code', 'sensorType')
    #En caso de no incluir estos campos no se aceptan filtros y/o no se aceptan busquedas
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SensorDetailSerializer
        return SensorSerializer

    def create(self, request):
        print(request.user)
        #No se puede crear via API
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True)
    def readings(self, request, pk=None):
        readings = SensorReading.objects.filter(sensor__id=pk)
        serializer = SensorReadingSerializer(readings, many=True)
        return Response(serializer.data)


class SensorReadingRead(viewsets.ReadOnlyModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingDetailSerializer
    permission_classes = (IsAuthenticated, AutomatizadorOrReadOnly, )
