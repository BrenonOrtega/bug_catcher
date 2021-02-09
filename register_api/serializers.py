from rest_framework import serializers
from .models import Error

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = '__all__'
        exclude = []
        
    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        #TODO: Replicate instance.field for other fields in Error model.
