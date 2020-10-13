from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', editProfile, name='editprofile'),
] 