"""app URL Configuration

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
from importlib import import_module

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter(trailing_slash=False)


def autodiscover():
    for app in settings.LOCAL_APPS:
        try:
            import_module(".".join((app, "api")))
        except ImportError:
            pass


autodiscover()
pair_view = TokenObtainPairView.as_view()
refresh_view = TokenRefreshView.as_view()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token", pair_view, name="token_obtain_pair"),
    path("api/token/refresh", refresh_view, name="token_refresh"),
    re_path(r"^api/", include(router.urls)),
]
