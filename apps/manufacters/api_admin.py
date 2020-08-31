# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .permissions import (
    AdminManufacters, AdminSpecificManufacterDetail,
    AdminSpecificManufacter
)

from .models import Manufacter
from django_module_attr.models import GenericData

from .serializers import (
    AdminManufacterSerializer, ManufacterCreateSerializer,
    AdminConfigSerializer
)


class AdminManufacterViewSet(ModelViewSet):
    queryset = Manufacter.objects.all()
    serializer_class = AdminManufacterSerializer
    permission_classes = (AdminManufacters,)

    filter_fields = ('type', 'enabled')
    search_fields = ('name', 'uuid')
    ordering_fields = ('name', 'created_at')
    ordering = 'name'

    def get_permissions(self):
        if self.detail:
            self.permission_classes = [AdminSpecificManufacterDetail]
        return super(AdminManufacterViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = ManufacterCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        manufacter = serializer.save()

        serializer = self.get_serializer(manufacter)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AdminManufacterConfigViewSet(GenericViewSet):
    queryset = GenericData.objects.all()
    serializer_class = AdminConfigSerializer
    permission_classes = (AdminManufacters | AdminSpecificManufacter,)

    def list(self, request, *args, **kwargs):
        manufacter = Manufacter.objects.get(pk=self.kwargs['manu_pk'])

        if not manufacter.config:
            raise Http404()

        serializer = AdminConfigSerializer(manufacter.config)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        manufacter = Manufacter.objects.get(pk=self.kwargs['manu_pk'])
        serializer = AdminConfigSerializer(manufacter.config, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(manufacter=manufacter)

        return Response(serializer.data)
