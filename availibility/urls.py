from django.urls import path
from .views import *

urlpatterns = [
    path('', availibility, name='availibility'),
    path('camps/', camp, name='camp')
]