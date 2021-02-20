from django.urls import path
from register_api import views

urlpatterns = [
    path('bugs', views.BugList.as_view()),
    path('bugs/<int:pk>/', views.BugDetails.as_view()),


    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped)
]


