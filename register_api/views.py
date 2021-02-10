from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Error
from .serializers import ErrorSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def ErrorsList(request):
    if request.method == 'GET':
        errors = Error.objects.all()
        serializer = ErrorSerializer(errors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ErrorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def ErrorDetail(request, pk):
    try:
        error = Error.objects.get(pk=pk)
    except Error.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ErrorSerializer(error)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = ErrorSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        error.delete()
        return HttpResponse(status=204)
