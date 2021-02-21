from django.conf import settings
from django.contrib.auth.models import User
from django.http.response import Http404
from django.contrib.auth import get_user 
from django.shortcuts import render
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView, View
from .models import Bug
from .serializers import BugReadSerializer, BugWriteSerializer, UserReadSerializer


class BugList(APIView):
    def get(self, request):
        bug = Bug.objects.all()
        serializer = BugReadSerializer(bug, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """ def post(self, request):
        serializer = BugWriteSerializer(data=request.data) """

    def post(self, request):
        author = get_user(request)

        if author.is_authenticated :
            serializer = BugWriteSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(author=author)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: return Response(status=status.HTTP_403_FORBIDDEN)

class BugDetails(APIView, mixins.DestroyModelMixin):
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

    def put(self, request, pk):
        bug = self.get_object(pk)
        serializer = BugWriteSerializer(bug, request.data)
        modifier = get_user(request)
        
        if modifier.is_authenticated:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: return Response(status=status.HTTP_403_FORBIDDEN)


#####################################################################################
class BugListPage(View):
    def get(self, request):
        bugs = Bug.objects.all()
        context = {"bugs": bugs}
        return render(request, "home.html", context)


class GetUserBugs(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserReadSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

