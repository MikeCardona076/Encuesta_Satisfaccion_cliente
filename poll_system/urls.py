from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', allTopics, name='allTopics'),
    path('questions/<int:pk>/', question, name='questions'),
    path('AnwserCreate/<int:pk>/', AnwserCreate.as_view(), name='AnwserCreate'),
]