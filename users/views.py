# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User, Group
from users.serializers import UserSerializer, UserSaveSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )
    __basic_fields = ('username', 'groups', 'is_staff')
    #En caso de no incluir estos campos no se aceptan filtros y/o no se aceptan busquedas
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return UserSaveSerializer
        return UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser, )
    __basic_fields = ('name')
    #En caso de no incluir estos campos no se aceptan filtros y/o no se aceptan busquedas
    #filter_fields = __basic_fields
    search_fields = __basic_fields