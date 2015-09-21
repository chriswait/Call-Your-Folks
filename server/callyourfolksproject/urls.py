from django.conf.urls import include, url
from django.contrib import admin

from callyourfolks.models import User, Contact, Call, Avatar
from callyourfolks.serializers import UserSerializer, ContactSerializer, CallSerializer, AvatarSerializer
from callyourfolks.viewsets import UserViewSet
from rest_framework import routers

callyourfolks_router = routers.DefaultRouter()
callyourfolks_router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^callyourfolks/', include('callyourfolks.urls')),
    url(r'^api/', include(callyourfolks_router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
