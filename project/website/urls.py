from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view),
    path('profile/', profile_view),
    path('password_change/', profile_view, name='password_change'), #FIX THIS LATER
    path('events/', events_view),
    path('clubs/', clubs_view),
]
