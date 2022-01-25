from django.contrib.auth.models import User
from rest_framework import serializers

from bookmark.models import Bookmark


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['title','url','created_at']