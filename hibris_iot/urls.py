"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from apps.auth_hibris_iot.api import TokenObtainPairView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Hibris IOT Api",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="edunola13@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)


class InfoApi(APIView):
    permission_classes = []

    def get(self, request):
        return Response(status=200)


urlpatterns = [
    url(r'^$', InfoApi.as_view(), name='info'),

    url(r'^api/$', InfoApi.as_view(), name='info_api'),
    url(r'^api/u/', include('django_module_users.urls')),
    url(r'^api/attr/', include('django_module_attr.urls')),
    url(r'^api/l/', include('apps.locations.urls')),
    url(r'^api/d/', include('apps.devices.urls')),
    url(r'^api/c/', include('apps.components.urls')),

    url(r'^api/o/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/o/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/o/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

        path('admin/', admin.site.urls),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
