# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import permissions


class SafeMethodOrIsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        return request.user.is_staff
