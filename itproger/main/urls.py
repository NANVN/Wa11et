from django.urls import path
from .views import *

urlpatterns = [
    path('', signup, name='home'),
    path('signin/', signin, name='login'),
    path('signout/', signout, name='logout'),
    path('about/', about, name='we'),
    path('calendar/', calendar, name='calendar'),
    path('goals/', goals, name='we')
]
