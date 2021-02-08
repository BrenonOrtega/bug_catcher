from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Error
from .serializers import ErrorSerializer

# Create your views here.
def ErrorsList(request):
    msg = ('''
            <h1>Hello, welcome to the brenon's bug catcher</h1>
            <p>
            long and boring string,
            just using to test this string
            assignment
            </p>
            ''')
    return HttpResponse(msg)
    """  if request_method =='GET':
        registers = Register.objects.all()
        serializer = ArticleSerializer (articles, many=True)
        return HttpResponse("Hello sir", registers) """

    
    
def ErrorDetail(request):
    return HttpResponse(Error)
