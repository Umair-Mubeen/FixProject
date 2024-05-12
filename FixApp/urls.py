from django.urls import path
from .views import *

from FixApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Logs', views.Logs, name='Logs'),
]