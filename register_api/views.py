from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Register
from . serializers import RegisterSerializer

# Create your views here.
def register_list(request):
    if request_method =='GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer (articles, many=True)
