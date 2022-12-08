from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('searchattendence/', views.searchAttendence, name='searchattendence'),
    path('account/', views.facultyProfile, name='account'),

    path('updateStudentRedirect/', views.updateStudentRedirect, name='updateStudentRedirect'),
    path('updatestudent/', views.updateStudent, name='updateStudent'),
    path('attendence/', views.takeAttendence, name='attendence'),
    path('registerstudent/', views.registerStudent, name='registerStudent'),
    # path('video_feed/', views.videoFeed, name='video_feed'),
    # path('videoFeed/', views.getVideo, name='videoFeed'),
]