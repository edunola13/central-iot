# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework_simplejwt.views import TokenViewBase
from .serializers import TokenObtainSerializer


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainSerializer
