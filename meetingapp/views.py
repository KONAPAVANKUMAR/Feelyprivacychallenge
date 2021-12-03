from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo 
    
    
# establishing connection 
# to the database
client = pymongo.MongoClient("mongodb://localhost:27017/") 
    
# Database name 
db = client["meeting"] 



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

def addIdField(thisCursor):
    thisList = list(thisCursor)
    for idx in range(len(thisList)):
        thisList[idx]['id'] = thisList[idx]['_id']
    return thisList

def managerHomePageView(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Please login to continue')
        return redirect('landingpage')
    if not request.user.is_staff:
        messages.add_message(request, messages.INFO, 'You are not authorized to view this page')
        return redirect('landingpage')
    currentManagerId = request.user.id
    meetings = db["meetingapp_meetingmodel"].find({'manager_id':currentManagerId})
    context = {'meetings':addIdField(meetings)}
    return render(request, 'meetingapp/managerhomepage.html',context)

def employeeHomePageView(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Please login to continue')
        return redirect('landingpage')
    if request.user.is_staff:
        messages.add_message(request, messages.INFO, 'You are not authorized to view this page')
        return redirect('landingpage')
    return render(request, 'meetingapp/employeehomepage.html')

def logoutUser(request):
    logout(request)
    return redirect('landingpage')

from .models import MeetingModel

def createMeeting(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Please login to continue')
        return redirect('landingpage')
    if not request.user.is_staff:
        messages.add_message(request, messages.INFO, 'You are not authorized to view this page')
        return redirect('landingpage')
    MeetingModel(datetime = request.POST['datetime'],manager = request.user).save()
    return redirect('managerhomepage')

def deleteMeeting(request,id):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Please login to continue')
        return redirect('landingpage')
    if not request.user.is_staff:
        messages.add_message(request, messages.INFO, 'You are not authorized to view this page')
        return redirect('landingpage')
    db["meetingapp_meetingmodel"].delete_one({'_id':ObjectId(id)})
    return redirect('managerhomepage')



