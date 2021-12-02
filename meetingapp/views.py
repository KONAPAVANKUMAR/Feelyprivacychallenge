from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def landingPageView(request):
    return render(request, 'meetingapp/landingpage.html')

def employeeSignup(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if password != repassword:
        messages.error(request, 'Passwords do not match')
        return redirect('/')
    if User.objects.filter(username=username).exists():
        messages.info(request, 'Username already exists')
        return redirect('/')
    User.objects.create_user(username=username, password=password,is_staff=False)
    messages.success(request, 'Account created successfully')
    return redirect('/')

def managerSignup(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if password != repassword:
        messages.error(request, 'Passwords do not match')
        return redirect('/')
    if User.objects.filter(username=username).exists():
        messages.info(request, 'Username already exists')
        return redirect('/')
    User.objects.create_user(username=username, password=password,is_staff=True)
    messages.success(request, 'Account created successfully')
    return redirect('/')

def managerLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_staff:
        login(request, user)
        return redirect('managerhomepage')
    else:
        messages.error(request, 'Invalid credentials')
        return redirect('/')

def employeeLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None and not user.is_staff:
        login(request, user)
        return redirect('employeehomepage')
    else:
        messages.error(request, 'Invalid credentials')
        return redirect('/')

def managerHomePageView(request):
    return render(request, 'meetingapp/managerhomepage.html')

def employeeHomePageView(request):
    return render(request, 'meetingapp/employeehomepage.html')

def logoutUser(request):
    logout(request)
    return redirect('landingpage')

