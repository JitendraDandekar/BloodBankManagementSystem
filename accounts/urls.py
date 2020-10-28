from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', editProfile, name='editprofile'),
    path('adminpanel/', admin_panel, name='adminpanel'),
    path('adminpanel/userprofile/<int:pk>/', user_profile, name='userprofile'),
    path('adminpanel/edits/<str:field>/<int:pk>/', edit_panel, name='editpanel'),
    path('adminpanel/delete/<str:field>/<int:pk>/', delete, name='delete'),
    path('blood-request/', blood_request, name='bloodrequest'),
    path('blood-request/details/<int:pk>/', request_panel, name='requestpanel')
] 