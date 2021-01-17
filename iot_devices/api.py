# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from django.http import Http404
from django.utils.translation import gettext as _
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django_module_common.utils.exceptions import ConflictError

from .clouds.hibris.base import (
    HibrisService,
    DeviceDoesNotExist, InvalidDeviceAccess,
    InvalidDeviceType, InvalidLocation
)

from .serializers import (
    RegisterDeviceSerializer,
    UnregisterDeviceSerializer
)


class RegisterDeviceView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        model_type = self.request.data.get('model_type', None)
        serializer_class = RegisterDeviceSerializer.get_for_type(model_type)
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        device_id = serializer.validated_data.pop('device_id')

        try:
            device = HibrisService(device_id).register(
                serializer.validated_data,
                user=request.user
            )

            return Response(
                {
                    'id': device.pk,
                    'manufacter': device.manufacter.pk
                },
                status=status.HTTP_201_CREATED
            )
        except DeviceDoesNotExist:
            raise ConflictError(detail=_('El dispositivo no existe'))
        except InvalidDeviceAccess:
            raise ConflictError(detail=_('No tiene acceso al dispositivo'))
        except InvalidDeviceType:
            raise ConflictError(detail=_('El tipo del dispositivo es incorrecto'))
        except InvalidLocation:
            raise ConflictError(detail=_('No tiene acceso a la ubicacion'))
        except Exception as e:
            logging.exception('Unregister Device: {}'.format(str(e)))
            raise ConflictError(detail=_('No se puede registrar el dispositivo'))

    def delete(self, request, format=None):
        serializer = UnregisterDeviceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        device_id = serializer.validated_data.pop('device_id')

        try:
            HibrisService(device_id).unregister(
                serializer.validated_data,
            )

            return Response(status=status.HTTP_204_NO_CONTENT)
        except DeviceDoesNotExist:
            raise ConflictError(detail=_('El dispositivo no existe'))
        except InvalidDeviceAccess:
            raise ConflictError(detail=_('No tiene acceso al dispositivo'))
        except ObjectDoesNotExist:
            raise Http404
        except Exception as e:
            logging.exception('Unregister Device: {}'.format(str(e)))
            raise ConflictError(detail=_('No se puede eliminar el dispositivo'))
