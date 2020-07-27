# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.utils.permissions import SafeMethodOrIsStaff

from apps.ir.models import IrControl, IrAction
from apps.ir.serializers import IrControlSerializer, IrActionSerializer


class IrControlViewSet(viewsets.ModelViewSet):
    permission_classes = (SafeMethodOrIsStaff,)

    queryset = IrControl.objects.all()
    serializer_class = IrControlSerializer

    __basic_fields = ('name', )
    filter_fields = __basic_fields
    search_fields = __basic_fields
    ordering_fields = __basic_fields + ('created_at',)
    ordering = 'name'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['get'], detail=True)
    def actions(self, request, pk=None):
        actions = IrAction.objects.filter(control__id=pk)
        serializer = IrActionSerializer(actions, many=True)
        return Response(serializer.data)


class IrActionViewSet(viewsets.ModelViewSet):
    permission_classes = (SafeMethodOrIsStaff,)

    queryset = IrAction.objects.all()
    serializer_class = IrActionSerializer

    __basic_fields = ('name', 'control', 'decode_type')
    filter_fields = __basic_fields
    search_fields = __basic_fields
    ordering_fields = __basic_fields + ('created_at',)
    ordering = 'name'

    @action(methods=['post'], detail=True, permission_classes=(IsAuthenticated,))
    def execute(self, request, pk=None):
        # Ejecutar codigo sobre device X

        serializer = IrActionSerializer()
        return Response(serializer.data)
