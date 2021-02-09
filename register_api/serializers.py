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
        instance.name = validated_data.get(')


a = (''' 
from register_api.models import Error                                           
from register_api.serializers import ErrorSerializer                            
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser from django.contrib.auth.models import User
import io          
b = User.objects.get(id=1)
>>> a = Error(name = 'erro de teste', slug = 'test', author= b, description = "teste testes")
>>> a.save()
>>> serializer = ErrorSerializer(a)
>>> json = JSONRenderer().render(serializer.data) 
>>> stream = io.BytesIO(json)



''')
