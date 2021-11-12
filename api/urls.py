"""django_code URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, re_path, include


from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import oauth2_provider
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication


from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="MyProjects API",
        default_version='v1',
        description="Hobby projects api",
    #   terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mpilkou@gmail.com"),
        license=openapi.License(name="Apache License Version 2.0"),
    ),
    public=True,
    permission_classes=( IsAuthenticated, ),
    authentication_classes=( SessionAuthentication, OAuth2Authentication, )
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('sudoku/', views.SudokuView.as_view()),
    path('test/', views.test),
    path('rest/', include('rest_framework.urls')),
]
