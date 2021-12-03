from django.urls import path
from .views import *
urlpatterns = [
    path('',landingPageView, name='landingpage'),
    path('employee/signup/', employeeSignup, name='employeesignup'),
    path('manager/signup/', managerSignup, name='managersignup'),
    path('manager/login/', managerLogin, name='managerlogin'),
    path('employee/login/', employeeLogin, name='employeelogin'),
    path('logoutuser/', logoutUser, name='logoutuser'),
    path('manager/', managerHomePageView, name='managerhomepage'),
    path('employee/', employeeHomePageView, name='employeehomepage'),
    path('employee/schedule/<int:id>/',employeeScheduleView, name='employeeschedulepage'),

    # crud operations
    path('meeting/create/', createMeeting, name='createmeeting'),
    path('meeting/<str:id>/delete/', deleteMeeting),
]