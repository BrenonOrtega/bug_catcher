from django.urls import path
from rest_framework.exceptions import ErrorDetail
""" from .views import ErrorDetail, ErrorsList """
from register_api import views

urlpatterns = [
    #path('errors', ErrorsList),
    #path('errors/<int:pk>', ErrorDetail) 
    path('errors', views.ErrorsList.as_view()),
    path('errors/<int:id>', views.ErrorDetails.as_view())
]

