from django.urls import path
from .views import *
urlpatterns = [
    path('',landingPageView, name='landingpage'),
]