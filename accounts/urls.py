from django.urls import path, include
from accounts import models
from accounts import views

urlpatterns = [
    path('student-register' , views.studentRegister , name = 'student-register'),
    path('student-login', views.studentLogin , name = 'student-login'),
    path('student-details', views.studentDetails, name = 'student-details'), 
    path('entrepreneur-register' , views.entrepreneurRegister , name = 'entrepreneur-register'),
    path('entrepreneur-login', views.entrepreneurLogin , name = 'entrepreneur-login'),
    path('entrepreneur-details', views.entrepreneurDetails, name = 'entrepreneur-details'),
    path('investor-register' , views.investorRegister , name = 'investor-register'),
    path('investor-details', views.investorDetails, name = 'investor-details'), 
    path('mentor-register' , views.mentorRegister , name = 'mentor-register'),
    path('mentor-details', views.mentorDetails, name = 'mentor-details'),    
    path('submit-project', views.submitProjectIdea , name = 'submit-project'),
    path('successful-registration' , views.registerResponse , name = 'successful-registration'),
    path('dashboard' , views.dashboard , name = 'dashboard'),
    path('logout' , views.logoutPage , name = 'logout'),
    path('investor/<int:pk>' , views.investor_single_details , name = 'investor')    
]