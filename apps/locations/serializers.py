# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy as _lazy
from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from .models import (
    Location, UserLocation
)

from django_module_users.serializers import UserMinSerializer

User = get_user_model()


class LocationMinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'loc_uuid', 'type', 'name', 'path', 'parent', 'order',
                  'enabled', 'created_at', 'updated_at',)


class LocationSerializer(serializers.ModelSerializer):
    parent = LocationMinSerializer(many=False, read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'loc_uuid', 'type', 'name', 'path', 'parent', 'order',
                  'enabled', 'created_at', 'updated_at',)
        read_only_fields = ['id', 'path', 'parent',
                            'created_at', 'updated_at']


class LocationCreateSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), write_only=True, many=False, required=False
    )

    class Meta:
        model = Location
        fields = ('id', 'type', 'name', 'order',
                  'enabled', 'parent',)

    def create(self, validated_data, user):
        with transaction.atomic():
            location = Location.objects.create(**validated_data)
            UserLocation.objects.create(
                location=location,
                user=user,
                access=UserLocation.ACCESS_OWNER
            )

        return location


# class ChangeParentSerializer(serializers.ModelSerializer):
#     parent = serializers.PrimaryKeyRelatedField(
#         queryset=Location.objects.all(), write_only=True, many=False, allow_null=True
#     )

#     class Meta:
#         model = Location
#         fields = ('parent',)

#     def validate_parent(self, value):
#         if value is None:
#             return value

#         if self.instance.id == value.id:
#             raise serializers.ValidationError(_('Ubicacion no valida como padre'))

#         return value

#     def save(self):
#         with transaction.atomic():
#             self.instance.change_parent(self.validated_data.get('parent', None))


class UserLocationSerializer(serializers.ModelSerializer):
    user = UserMinSerializer(many=False, read_only=True)
    access = serializers.ChoiceField(choices=(
        (UserLocation.ACCESS_ADMIN, _lazy('Administrador')),
        (UserLocation.ACCESS_USER, _lazy('User')),
        (UserLocation.ACCESS_READ, _lazy('Lectura')),), default=UserLocation.ACCESS_USER)

    class Meta:
        model = UserLocation
        fields = ('id', 'user', 'access', 'enabled')


class UserLocationCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, many=False
    )
    access = serializers.ChoiceField(choices=(
        (UserLocation.ACCESS_ADMIN, _lazy('Administrador')),
        (UserLocation.ACCESS_USER, _lazy('User')),
        (UserLocation.ACCESS_READ, _lazy('Lectura')),), default=UserLocation.ACCESS_USER)

    class Meta:
        model = UserLocation
        fields = ('user', 'access')
