from rest_framework import serializers
from .models import Bug

class BugWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ['bug_name', 'description', 'status']

class BugReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        exclude = ['id']
