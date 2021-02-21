from django.http.response import Http404
from django.contrib.auth import get_user
from rest_framework import status
from rest_framework.views import APIView, View
from rest_framework.response import Response
from .serializers import BugReadSerializer, BugWriteSerializer
from .models import Bug

class BugList(APIView):
    def get(self, request):
        bug = Bug.objects.all()
        serializer = BugReadSerializer(bug, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        author = get_user(request)
        if author.is_authenticated :
            serializer = BugWriteSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(author=author)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: return Response(status=status.HTTP_403_FORBIDDEN)

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
from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from urllib.parse import urlencode
from django.conf import settings
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/bugs")
    else:
        return render(request, "index.html")

def logout(request):
    log_out(request)
    return_to = urlencode({"returnTo": request.build_absolute_uri("/")})
    logout_url = "https://{}/v2/logout?client_id={}&{}".format(
        settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to,
    )
    return HttpResponseRedirect(logout_url)

@method_decorator(login_required, name='get')
class BugListView(View):
    def get(self, request):
        bugs = Bug.objects.all()
        print(bugs)
        context = {"bugs": bugs}
        print(context)
        return render(request, "home.html", context)
