from django.contrib.auth.models import Group
from rest_framework.serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "groups"]


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
