from django.urls import path
from .views import *

urlpatterns = [
    path('', TestCreate.as_view(), name='medical'),
]