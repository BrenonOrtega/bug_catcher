from rest_framework import serializers
from .models import Error

class ErrorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ['name', 'slug', 'author', 'email', 'date', 'last_update', 'description', 'status', ]
