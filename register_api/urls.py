from django.urls import path
from .views import ErrorsList

urlpatterns = [
    path('errors', ErrorsList),

    
]

