from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

public_router = DefaultRouter()
internal_router = DefaultRouter()

urlpatterns = [
    path("", include(public_router.urls)),
    path("internal/", include(internal_router.urls)),
]
