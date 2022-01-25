from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime

from bookmark.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookmarkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    private = serializers.BooleanField(required=False)
    url = serializers.CharField(required=False)
    # tags = serializers.ListField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Bookmark` instance, given the validated data.
        """
        return Bookmark.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Bookmark` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.private = validated_data.get('private', instance.private)
        instance.language = validated_data.get('language', instance.language)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = datetime.now()
        instance.save()
        return instance

    def delete(self):
        return "Bookmark deleted"

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tag = serializers.CharField(required=False, allow_blank=True, max_length=50)

    def create(self, validated_data):
        """
        Create and return a new `Bookmark` instance, given the validated data.
        """
        return Tag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Bookmark` instance, given the validated data.
        """
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance

    def delete(self):
        return "Tag deleted"