from register_api.models import Error
from register_api.serializers import ErrorSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
import io

#instancia um objeto do meu usuário
user = User.objects.get(id=1) 
error = Error(name='erro atoa', slug= 'teste7', author=user, email=user.email, description='')
error.save()

serializer = ErrorSerializer(error)
json = JSONRenderer().render(serializer.data)
stream = io.BytesIO(json)

data = JSONParser().parse(stream)
serializer = ErrorSerializer(data=data)
valid_data = serializer.validated_data if serializer.is_valid() else "not validated"

print(valid_data, f'is_valid()? {serializer.is_valid()}')

#   To run from python terminal using manage.py shell
#   exec(open('model_serializer.py').read())

