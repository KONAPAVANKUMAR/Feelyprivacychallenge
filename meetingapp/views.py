from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def landingPageView(request):
    return render(request, 'meetingapp/landingpage.html')


