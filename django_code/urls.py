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
from django.contrib import admin
from django.urls import path, include

# from django.shortcuts import redirect
# from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.views import LoginView
from oauth2_provider.views import AuthorizationView
# from oauth2_provider.
# oauth2_views.AuthorizationView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    # path('sudoku/', include('sudoku.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('accounts/', include('accounts.urls')),
    path('accounts/login/', LoginView.as_view(template_name='login.html')),
    # path('accounts/', include('django.contrib.auth.urls')),
]
