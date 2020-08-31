# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet

from .models import Manufacter

from .serializers import (
    ManufacterMinSerializer
)


class ManufacterViewSet(ModelViewSet):
    queryset = Manufacter.objects.filter(enabled=True)
    serializer_class = ManufacterMinSerializer

    filter_fields = ('type',)
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at')
    ordering = 'name'
