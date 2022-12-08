import re
from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from multiselectfield import MultiSelectField
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime as dt
from datetime import datetime
from .forms import *
from .models import Student, Attendence, Time, Subject
from .filters import AttendenceFilter
from django.views.decorators import gzip
import cv2
import threading
from .recognizer import Recognizer
#from .recognizers import Recognizer

    
def registerPage(request):
    lecturerForm = CreateLecturerForm()

    if request.method == 'POST':
        lecturerForm = CreateLecturerForm(request.POST)
        if lecturerForm.is_valid():
            lecturerForm.save()
            return redirect('login')
    context = {'lecturerForm':lecturerForm}
    return render(request, 'attendence_sys/register.html', context)
    
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'attendence_sys/login.html', context)

@login_required(login_url = 'login')
def home(request):
    studentForm = CreateStudentForm()
    timeForm = TimeForm()
    subjectForm = SubjectForm()

    if request.method == 'POST':
        studentForm = CreateStudentForm(data = request.POST, files=request.FILES)
        #timeForm = TimeForm(data = request.POST, files=request.FILES)
        #subjectForm = SubjectForm(request.POST)
        # print(request.POST)
        stat = False 
        try:
            student = Student.objects.get(matricno = request.POST['matricno'])
            stat = True
        except:
            stat = False
        if  studentForm.is_valid() and (stat == False):
            studentForm.save()
            #timeForm.save()
            #subjectForm.save()

            name = studentForm.cleaned_data.get('name')
            subject = studentForm.cleaned_data.get('subject')
            messages.success(request, 'Student ' + name + ' was successfully added.')
            return redirect('home')
        else:
            messages.error(request, 'Student with the Matric No. '+request.POST['matricno']+' already exists.')
            return redirect('home')

    context = {'studentForm':studentForm, 'timeForm':timeForm, 'subjectForm':subjectForm}
    return render(request, 'attendence_sys/home.html', context)

@login_required(login_url = 'login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def updateStudentRedirect(request):
    context = {}
    if request.method == 'POST':
        try:
            matricno = request.POST['matricno']
            program = request.POST['program']
            subjects = request.POST['subjects']
            student = Student.objects.get(matricno = matricno, program = program, subjects =subjects)
            updateStudentForm = CreateStudentForm(instance=student)
            context = {'form':updateStudentForm, 'prev_matricno':matricno, 'student':student, 'subjects':subjects}
        except:
            messages.error(request, 'Student Not Found')
            return redirect('attendence_sys/student_update.html')
    return render(request, 'attendence_sys/student_update.html', context)

@login_required(login_url = 'login')
def updateStudent(request):
    if request.method == 'POST':
        context = {}
        try:
            student = Student.objects.get(matricno = request.POST['prev_matricno'])
            updateStudentForm = CreateStudentForm(data = request.POST, files=request.FILES, instance = student)
            if updateStudentForm.is_valid():
                updateStudentForm.save()
                messages.success(request, 'Updation Success')
                return redirect('home')
        except:
            messages.error(request, 'Updation Unsucessfull')
            return redirect('home')
    return render(request, 'attendence_sys/student_update.html', context)


@login_required(login_url = 'login')
def takeAttendence(request):

    if request.method == 'POST':

        details = {
            'subjects':request.POST['subjects'],
            'classday':request.POST['classday'],
            'classstart':request.POST['classstart'],
            'classend':request.POST['classend'],
            'faculty':request.user.faculty,
            }
        #if Attendence.objects.filter(section = details['section'], subject = details['subject']).count() != 0 :
            #messages.error(request, "Attendence already recorded.")
            #return redirect('home')
        #else:
        students = Student.objects.filter(subjects = details['subjects'])
        times = Time.objects.filter(day = details['classday'], start = details['classstart'], end = details['classend'])
        now = datetime.now()
        names = Recognizer(details)
        for student in students:
            if str(student.matricno) in names:
                attendence = Attendence(Faculty_Name = request.user.faculty,
                name = student.name,
                date = now.strftime("%d/%m/%Y"),
                time = now.strftime("%H:%M:%S"),
                matricno = str(student.matricno),
                semester = str(student.semester),
                classday = details['classday'],
                classstart = details['classstart'],
                classend = details['classend'],
                program = student.program,
                year = student.year,
                section = str(student.section),
                subjects = details['subjects'],
                status = 'Present',
                
                )
                attendence.save()  
            else:
                attendence = Attendence(Faculty_Name = request.user.faculty,
                name = student.name,
                date = now.strftime("%d/%m/%Y"),
                time = '-',
                matricno = str(student.matricno),
                semester = str(student.semester), 
                classday = details['classday'], 
                classstart = details['classstart'],
                classend = details['classend'],
                program = student.program,
                year = student.year,
                section = str(student.section),
                subjects = details['subjects'],)
                attendence.save()
        attendences = Attendence.objects.filter(subjects = details['subjects'])
        context = {"attendences":attendences, "ta":True}
        messages.success(request, "Attendence taking Successful")
        return render(request, 'attendence_sys/attendence.html', context)        
    context = {}
    return render(request, 'attendence_sys/home.html', context)

def searchAttendence(request):
    attendences = Attendence.objects.all()
    myFilter = AttendenceFilter(request.GET, queryset=attendences)
    attendences = myFilter.qs
    context = {'myFilter':myFilter, 'attendences': attendences, 'ta':False}
    return render(request, 'attendence_sys/attendence.html', context)


def facultyProfile(request):
    faculty = request.user.faculty
    form = FacultyForm(instance = faculty)
    context = {'form':form}
    return render(request, 'attendence_sys/facultyForm.html', context)

def registerStudent(request):
    studentForm = CreateStudentForm()

    if request.method == 'POST':
        studentForm = CreateStudentForm(data = request.POST, files=request.FILES)
        # print(request.POST)
        stat = False 
        try:
            student = Student.objects.get(matricno = request.POST['matricno'], subjects = request.POST['subjects'])
            stat = True
        except:
            stat = False
        if  studentForm.is_valid() and (stat == False):
            studentForm.save()
            name = studentForm.cleaned_data.get('name')
            messages.success(request, 'Student ' + name + ' was successfully added.')
            return redirect('registerStudent')
        else:
            messages.error(request, 'Student with the Matric No. ' + request.POST['matricno'] + ' already exists.')
            return redirect('registerStudent')

    context = {'studentForm':studentForm}
    return render(request, 'attendence_sys/registerStudent.html', context)

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         ret,image = self.video.read()
#         ret,jpeg = cv2.imencode('.jpg',image)
#         return jpeg.tobytes()


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield(b'--frame\r\n'
#         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# @gzip.gzip_page
# def videoFeed(request):
#     if request.method == 'POST':
#         try:
#             return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
#         except:
#             print("aborted")
    

    

# def getVideo(request):
#     if request.method == 'POST':
#         #render(request, 'attendence_sys/videoFeed.html')
#         details = {
#             'subjects':request.POST['subjects'],
#             'classday':request.POST['classday'],
#             'classstart':request.POST['classstart'],
#             'classend':request.POST['classend'],
#             'faculty':request.user.faculty,
#             }
#         #if Attendence.objects.filter(section = details['section'], subject = details['subject']).count() != 0 :
#             #messages.error(request, "Attendence already recorded.")
#             #return redirect('home')
#         #else:
#         students = Student.objects.filter(subjects = details['subjects'])
#         times = Time.objects.filter(day = details['classday'], start = details['classstart'], end = details['classend'])
#         now = datetime.now()
#         names = Recognizer(details)
#         render('attendence_sys/videoFeed.html')
#         for student in students:
#             if str(student.matricno) in names:
#                 attendence = Attendence(Faculty_Name = request.user.faculty,
#                 name = student.name,
#                 date = now.strftime("%d/%m/%Y"),
#                 time = now.strftime("%H:%M:%S"),
#                 matricno = str(student.matricno),
#                 semester = str(student.semester),
#                 classday = details['classday'],
#                 classstart = details['classstart'],
#                 classend = details['classend'],
#                 program = student.program,
#                 year = student.year,
#                 section = str(student.section),
#                 subjects = details['subjects'],
#                 status = 'Present',
                
#                 )
#                 attendence.save()  
#             else:
#                 attendence = Attendence(Faculty_Name = request.user.faculty,
#                 name = student.name,
#                 date = now.strftime("%d/%m/%Y"),
#                 time = '-',
#                 matricno = str(student.matricno),
#                 semester = str(student.semester), 
#                 classday = details['classday'], 
#                 classstart = details['classstart'],
#                 classend = details['classend'],
#                 program = student.program,
#                 year = student.year,
#                 section = str(student.section),
#                 subjects = details['subjects'],)
#                 attendence.save()
#         attendences = Attendence.objects.filter(subjects = details['subjects'])
#         context = {"attendences":attendences, "ta":True}
#         messages.success(request, "Attendence taking Successful")
#         return render(request, 'attendence_sys/attendence.html', context)        
#     context = {}
#     return render(request, 'attendence_sys/home.html', context)
    
    