# -*- coding: utf-8 -*-
from __future__ import unicode_literals

LOC_TYPE_OTHER = "OTHER"
LOC_TYPE_HOME = "HOME"
LOC_TYPE_ROOM = "ROOM"

LOC_TYPE_CHOICES = (
    (LOC_TYPE_OTHER, 'Otro'),
    (LOC_TYPE_HOME, 'Casa'),
    (LOC_TYPE_ROOM, 'Habitacion'),
)

ACCESS_OWNER = "OWNER"
ACCESS_ADMIN = "ADMIN"
ACCESS_USER = "USER"
ACCESS_READ = "READ"

ACCESS_CHOICES = (
    (ACCESS_OWNER, 'Owner'),
    (ACCESS_ADMIN, 'Administrador'),
    (ACCESS_USER, 'Usuario'),
    (ACCESS_READ, 'Lectura'),
)
