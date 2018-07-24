# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from ir.models import IrControl, IrAction
from ir.serializers import IrControlSerializer, IrActionSerializer
from ir.permissions import ControlPermissions, ActionPermissions


class IrControlViewSet(viewsets.ModelViewSet):
    queryset = IrControl.objects.all()
    serializer_class = IrControlSerializer
    permission_classes = (IsAuthenticated, ControlPermissions)
    
    __basic_fields = ('name', )
    #En caso de no incluir estos campos no se aceptan filtros y/o no se aceptan busquedas
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['get'], detail=True)
    def actions(self, request, pk=None):
        actions = IrAction.objects.filter(control__id=pk)
        serializer = IrActionSerializer(actions, many=True)
        return Response(serializer.data)


class IrActionViewSet(viewsets.ModelViewSet):
    queryset = IrAction.objects.all()
    serializer_class = IrActionSerializer
    permission_classes = (IsAuthenticated, ActionPermissions) 

    __basic_fields = ('name', 'control', 'decodeType')
    #En caso de no incluir estos campos no se aceptan filtros y/o no se aceptan busquedas
    filter_fields = __basic_fields
    search_fields = __basic_fields