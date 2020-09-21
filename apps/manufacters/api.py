# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Manufacter

from .serializers import (
    ManufacterMinSerializer
)


class ManufacterViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Manufacter.objects.filter(enabled=True)
    serializer_class = ManufacterMinSerializer

    filter_fields = ('type',)
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at')
    ordering = 'name'
