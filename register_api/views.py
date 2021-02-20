import jwt
from .models import Bug
from functools import wraps
from django.http import JsonResponse
from django.http.response import Http404
from django.contrib.auth import get_user
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from .serializers import BugReadSerializer, BugWriteSerializer



class BugList(APIView):
    @permission_classes("read:messages")
    def get(self, request):
        bug = Bug.objects.all()
        serializer = BugReadSerializer(bug, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes('read:messages')
    def post(self, request):
        author = get_user(request)
        if author.is_authenticated :
            serializer = BugWriteSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(author=author)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: raise Exception("User must be logged in to post.")

class BugDetails(APIView):
    def get_object(self, pk):
        try:
            bug_object = Bug.objects.get(pk=pk)
            return bug_object
        except:
            raise Http404

    def get(self, request, pk):
        bug = self.get_object(pk)
        serializer = BugReadSerializer(bug)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes(['read:messages', 'write:messages'])
    def put(self, request, pk):
        bug = self.get_object(pk)
        serializer = BugWriteSerializer(bug, request.data)
        modifier = get_user(request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

def get_token_auth_header(request):
    #Obtains the Access Token from the Authorization Header
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]
    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope


###################################################################################################
#Teste#######################################
@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})


@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})
