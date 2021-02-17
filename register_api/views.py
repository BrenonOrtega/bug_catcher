from django import http
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
import rest_framework
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from .models import Error
from .serializers import ErrorSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

class ErrorsList(APIView):
    def get(self, request):
        errors = Error.objects.all().order_by("id")
        serializer = ErrorSerializer(errors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ErrorSerializer(data=request.data)
        if serializer.is_Valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ErrorDetails(APIView):
    def get_object(self, id):
        try:
            return Error.objects.get(id=id)
        except Error.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id):
        error = self.get_object(id)
        serializer = ErrorSerializer(error)
        return Response(serializer.data)

    def put(self, request, id):
        error = self.get_object(id)
        serializer = ErrorSerializer(error, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        error = self.get_object(id)
        serializer = ErrorSerializer(error, data=request.data)
        

# Create your views here.

'''
@api_view(['GET', 'POST'])
def ErrorsList(request):
    if request.method == 'GET':
        errors = Error.objects.all()
        serializer = ErrorSerializer(errors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ErrorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def ErrorDetail(request, pk):
    try:
        error = Error.objects.get(pk=pk)
    except Error.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ErrorSerializer(error)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ErrorSerializer(error, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        error.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    '''
