from django.urls import path
from .views import *

urlpatterns = [
    path('', account, name='account'),
    path('home/', main, name='home'),
    path('signout/', signout, name='logout'),
    path('about/', about, name='we'),
    path('calendar/', calendar, name='calendar'),
    path('goals/', goals)
]
