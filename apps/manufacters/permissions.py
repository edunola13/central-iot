# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_module_users.permissions import RolePermission, RolePermissionDetail


class AdminManufacters(RolePermission):
    permission_names = ['admin_manufacters']


class AdminSpecificManufacterDetail(RolePermissionDetail):
    permission_names = ['admin_specific_manufacters']
    detail_pk = 'pk'


class AdminSpecificManufacter(RolePermission):
    permission_names = ['admin_specific_manufacters']
    detail_pk = 'manu_pk'
