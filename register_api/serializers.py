from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from .models import Bug

class BugWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ["bug_name", "description", "status"]

class BugReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = "__all__"
        #exclude = ['id']

class UserReadSerializer(serializers.ModelSerializer):
    bugs = BugReadSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "bugs")
