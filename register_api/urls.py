from django.urls import path
from register_api import auth0backend, views


urlpatterns = [
    path('bugs/', views.BugList.as_view()),
    path('bugs/<int:pk>/', views.BugDetails.as_view()),
    path('', views.index)

]
