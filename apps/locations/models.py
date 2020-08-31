# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.auth import get_user_model

from .constants import (
    LOC_TYPE_OTHER, LOC_TYPE_HOME, LOC_TYPE_ROOM,
    LOC_TYPE_CHOICES,
    ACCESS_OWNER, ACCESS_ADMIN, ACCESS_READ,
    ACCESS_USER,
    ACCESS_CHOICES
)

User = get_user_model()


class Location (models.Model):
    LOC_TYPE_OTHER = LOC_TYPE_OTHER
    LOC_TYPE_HOME = LOC_TYPE_HOME
    LOC_TYPE_ROOM = LOC_TYPE_ROOM

    loc_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    type = models.CharField(max_length=10,
                            default=LOC_TYPE_OTHER,
                            choices=LOC_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=255, null=True)

    parent = models.ForeignKey("Location",
                               null=True,
                               related_name="childs",
                               on_delete=models.PROTECT)
    order = models.PositiveIntegerField(default=0)

    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Location, self).save(*args, **kwargs)
        if self.path is None:
            self.build_path()
            self.save()

    def build_path(self):
        path = "/"
        if self.parent:
            path = self.parent.path
        self.path = path + str(self.id) + "/"

    def update_path(self):
        self.build_path()
        self.save()
        for child in self.childs.all():
            child.update_path()

    def change_parent(self, parent):
        self.parent = parent
        self.update_path()

    class Meta:
        ordering = ('name',)


class UserLocation (models.Model):
    ACCESS_OWNER = ACCESS_OWNER
    ACCESS_ADMIN = ACCESS_ADMIN
    ACCESS_USER = ACCESS_USER
    ACCESS_READ = ACCESS_READ

    access = models.CharField(max_length=10,
                              default=ACCESS_READ,
                              choices=ACCESS_CHOICES)
    location = models.ForeignKey(Location,
                                 related_name="users",
                                 on_delete=models.PROTECT)
    user = models.ForeignKey(User,
                             related_name="locations",
                             on_delete=models.PROTECT)

    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
