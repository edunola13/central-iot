# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

LOC_TYPE_OTHER = "OTHER"
LOC_TYPE_HOME = "HOME"
LOC_TYPE_ROOM = "ROOM"

LOC_TYPE_CHOICES = (
    (LOC_TYPE_OTHER, _('Otro')),
    (LOC_TYPE_HOME, _('Casa')),
    (LOC_TYPE_ROOM, _('Habitacion')),
)

ACCESS_OWNER = "OWNER"
ACCESS_ADMIN = "ADMIN"
ACCESS_USER = "USER"
ACCESS_READ = "READ"

ACCESS_CHOICES = (
    (ACCESS_OWNER, _('Owner')),
    (ACCESS_ADMIN, _('Administrador')),
    (ACCESS_USER, _('Usuario')),
    (ACCESS_READ, _('Lectura')),
)
