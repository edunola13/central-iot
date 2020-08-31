# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import action
from django.db import transaction

from django_module_common.utils.exceptions import ConflictError

from .models import (
    Location, UserLocation
)

from .serializers import (
    LocationSerializer, LocationCreateSerializer,
    # ChangeParentSerializer,
    UserLocationSerializer, UserLocationCreateSerializer
)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    filter_fields = {
        'loc_uuid': ['exact'],
        'type': ['exact'],
        'enabled': ['exact'],
        'parent': ['exact', 'isnull']
    }
    search_fields = ('name', 'path')
    ordering_fields = ('name', 'order', 'created_at')
    ordering = 'name'

    def get_queryset(self):
        return self.queryset.filter(
            users__user=self.request.user,
            users__enabled=True
        )

    def create(self, request, *args, **kwargs):
        serializer = LocationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # CHECK PERMISSION IN PARENT, ONLY IF NOT NONE

        location = serializer.create(
            serializer.validated_data,
            request.user
        )

        serializer = self.get_serializer(location)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # UPDATE: CHECK ACCESS, only OWNER o ADMIN

    # CHECK ACCESS, depends if is a ROOT (OWNER) or PARENT (OWNER o ADMIN)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            with transaction.atomic():
                instance.users.all().delete()
                instance.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            raise ConflictError(detail=_('No se puede eliminar la ubicacion'))

    # CHECK ACCESS, only available if parent not NONE, if a ROOT cant associate to other ROOT
    # @action(methods=['put'], detail=True, url_path='parent')
    # def parent(self, request, pk=None, *args, **kwargs):
    #     location = self.get_object()
    #     serializer = ChangeParentSerializer(location, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     serializer = self.get_serializer(location)

    #     return Response(serializer.data)


class UsersLocationViewSet(ModelViewSet):
    queryset = UserLocation.objects.all().select_related('user', 'location')
    serializer_class = UserLocationSerializer

    filter_fields = ('user',)
    ordering_fields = ('user__username', 'created_at')
    ordering = 'user__username'

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return UserLocation.objects.all()

        return UserLocation.objects.filter(location__pk=self.kwargs['location_pk'])

    # CHECK PERMISSIONS
    # CHECK THAT DONT EDIT YOURSELF

    def create(self, request, *args, **kwargs):
        serializer = UserLocationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_location = serializer.save(location=Location.objects.get(pk=self.kwargs['location_pk']))

        serializer = self.get_serializer(user_location)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
