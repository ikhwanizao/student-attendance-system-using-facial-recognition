from django.db.models.deletion import CASCADE
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta
import math


SUBJECT = (
    ('Pengurusan Projek','Pengurusan Projek'),
    ('Pengurusan Perhubungan Pelanggan','Pengurusan Perhubungan Pelanggan'),
    ('Sistem Bantuan Keputusan','Sistem Bantuan Keputusan'),
    ('English for Higher Education', 'English for Higher Education'),
    ('Pengajian Islam','Pengajian Islam'),
    ('Pengajian Moral','Pengajian Moral'),
    ('Kenegaraan dan Pembangunan Mutakhir Malaysia','Kenegaraan dan Pembangunan Mutakhir Malaysia'),
    ('Prinsip Teknologi Maklumat','Prinsip Teknologi Maklumat'),
    ('Pengaturcaraan Komputer','Pengaturcaraan Komputer'),
    ('Struktur Diskrit','Struktur Diskrit'),
    ('Senibina Komputer','Senibina Komputer'),
    ('Falsafah Dan Isu Semasa','Falsafah Dan Isu Semasa'),
    ('Creativity & Innovation', 'Creativity & Innovation'),
    ('Sistem Maklumat Pengurusan', 'Sistem Maklumat Pengurusan'),
    ('Statistik','Statistik'),
    ('Kejuruteraan Perisian','Kejuruteraan Perisian'),
    ('Struktur Data dan Algoritma','Struktur Data dan Algoritma'),
    ('Essential Academic English','Essential Academic English'),
    ('Penghayatan, Etika dan Peradaban','Penghayatan, Etika dan Peradaban'),
    ('Interaksi Manusia-Komputer', 'Interaksi Manusia-Komputer'),
    ('Etika Profesional dan Keselamatan Pekerjaan','Etika Profesional dan Keselamatan Pekerjaan'),
    ('Analisis dan Rekabentuk Sistem','Analisis dan Rekabentuk Sistem'),
    ('Pengaturcaraan Berorientasikan Objek', 'Pengaturcaraan Berorientasikan Objek'),
    ('Sistem Pengoperasian','Sistem Pengoperasian'),
    ('Asas Keselamatan Maklumat','Asas Keselamatan Maklumat'),
    ('Pembangunan Web', 'Pembangunan Web'),
    ('Rangkaian dan Komunikasi Data','Rangkaian dan Komunikasi Data'),
    ('Sistem Pangkalan Data','Sistem Pangkalan Data'),
    ('Pengaturcaraan JAVA', 'Pengaturcaraan JAVA'),
    ('English for Technical Purposes','English for Technical Purposes'),
    ('Keusahawanan','Keusahawanan'),
    ('Pembangunan Aplikasi Mudah Alih','Pembangunan Aplikasi Mudah Alih'),
    ('Metodologi Penyelidikan Projek','Metodologi Penyelidikan Projek'),
    ('English for Occupational Purposes','English for Occupational Purposes'),
    ('Perancangan Sumber Enterprise','Perancangan Sumber Enterprise'),
    ('Projek Sarjana Muda', 'Projek Sarjana Muda'),
    ('Kecerdasan Buatan', 'Kecerdasan Buatan'),
    ('Pelombongan Data','Pelombongan Data'),
    ('Pembangunan Sistem Fuzzy','Pembangunan Sistem Fuzzy'),
    ('Pembelajaran Mesin','Pembelajaran Mesin'),
    ('Pembelajaran Mendalam','Pembelajaran Mendalam'),
    ('Sains Data','Sains Data')
)

CLASSSTARTTIME = (
        ('08:00 am','08:00 am'),
        ('09:00 am','09:00 am'),
        ('10:00 am','10:00 am'),
        ('11:00 am','11:00 am'),
        ('12:00 pm','12:00 pm'),
        ('01:00 pm','01:00 pm'),
        ('02:00 pm','02:00 pm'),
        ('03:00 pm','03:00 pm'),
        ('04:00 pm','04:00 pm'),
        ('05:00 pm','05:00 pm'),
        ('06:00 pm','06:00 pm'),
    )
CLASSENDTIME = (
        ('08:00 am','08:00 am'),
        ('09:00 am','09:00 am'),
        ('10:00 am','10:00 am'),
        ('11:00 am','11:00 am'),
        ('12:00 pm','12:00 pm'),
        ('01:00 pm','01:00 pm'),
        ('02:00 pm','02:00 pm'),
        ('03:00 pm','03:00 pm'),
        ('04:00 pm','04:00 pm'),
        ('05:00 pm','05:00 pm'),
        ('06:00 pm','06:00 pm'),
    )

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Sunday', 'Sunday'),
)

class Subject(models.Model):
    subjectname = models.CharField(max_length=200, null=True, choices=SUBJECT)

    def __str__(self):
        return str(self.subjectname)
        
def user_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = instance.firstname + instance.lastname
    filename = name +'.'+ ext 
    return 'Faculty_Images/{}'.format(filename)

class Faculty(models.Model):

    user = models.OneToOneField(User, null = True, blank = True, on_delete= models.CASCADE)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to=user_directory_path ,null=True, blank=True)

    def __str__(self):
        return str(self.firstname + " " + self.lastname)


def student_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = instance.matricno # + "_" + instance.branch + "_" + instance.year + "_" + instance.section
    filename = name +'.'+ ext 
    return 'Student_Images/{}/{}'.format(instance.subjects,filename)

class Student(models.Model):

    PROGRAM = (
        ('BIT','BIT'),
        ('BIP','BIP'),
        ('BIW','BIW'),
        ('BIS','BIS'),
        ('BIM','BIM'),
    )
    YEAR = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
    )
    SECTION = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),
        ('14','14'),
        ('15','15'),
        ('16','16'),
        ('17','17'),
        ('18','18'),
        ('19','19'),
        ('20','20'),
        ('21','21'),
        ('22','22'),
        ('23','23'),
        ('24','24'),
    )
    SUBJECT = (
    ('Pengurusan Projek','Pengurusan Projek'),
    ('Pengurusan Perhubungan Pelanggan','Pengurusan Perhubungan Pelanggan'),
    ('Sistem Bantuan Keputusan','Sistem Bantuan Keputusan'),
    ('English for Higher Education', 'English for Higher Education'),
    ('Pengajian Islam','Pengajian Islam'),
    ('Pengajian Moral','Pengajian Moral'),
    ('Kenegaraan dan Pembangunan Mutakhir Malaysia','Kenegaraan dan Pembangunan Mutakhir Malaysia'),
    ('Prinsip Teknologi Maklumat','Prinsip Teknologi Maklumat'),
    ('Pengaturcaraan Komputer','Pengaturcaraan Komputer'),
    ('Struktur Diskrit','Struktur Diskrit'),
    ('Senibina Komputer','Senibina Komputer'),
    ('Falsafah Dan Isu Semasa','Falsafah Dan Isu Semasa'),
    ('Creativity & Innovation', 'Creativity & Innovation'),
    ('Sistem Maklumat Pengurusan', 'Sistem Maklumat Pengurusan'),
    ('Statistik','Statistik'),
    ('Kejuruteraan Perisian','Kejuruteraan Perisian'),
    ('Struktur Data dan Algoritma','Struktur Data dan Algoritma'),
    ('Essential Academic English','Essential Academic English'),
    ('Penghayatan, Etika dan Peradaban','Penghayatan, Etika dan Peradaban'),
    ('Interaksi Manusia-Komputer', 'Interaksi Manusia-Komputer'),
    ('Etika Profesional dan Keselamatan Pekerjaan','Etika Profesional dan Keselamatan Pekerjaan'),
    ('Analisis dan Rekabentuk Sistem','Analisis dan Rekabentuk Sistem'),
    ('Pengaturcaraan Berorientasikan Objek', 'Pengaturcaraan Berorientasikan Objek'),
    ('Sistem Pengoperasian','Sistem Pengoperasian'),
    ('Asas Keselamatan Maklumat','Asas Keselamatan Maklumat'),
    ('Pembangunan Web', 'Pembangunan Web'),
    ('Rangkaian dan Komunikasi Data','Rangkaian dan Komunikasi Data'),
    ('Sistem Pangkalan Data','Sistem Pangkalan Data'),
    ('Pengaturcaraan JAVA', 'Pengaturcaraan JAVA'),
    ('English for Technical Purposes','English for Technical Purposes'),
    ('Keusahawanan','Keusahawanan'),
    ('Pembangunan Aplikasi Mudah Alih','Pembangunan Aplikasi Mudah Alih'),
    ('Metodologi Penyelidikan Projek','Metodologi Penyelidikan Projek'),
    ('English for Occupational Purposes','English for Occupational Purposes'),
    ('Perancangan Sumber Enterprise','Perancangan Sumber Enterprise'),
    ('Projek Sarjana Muda', 'Projek Sarjana Muda'),
    ('Kecerdasan Buatan', 'Kecerdasan Buatan'),
    ('Pelombongan Data','Pelombongan Data'),
    ('Pembangunan Sistem Fuzzy','Pembangunan Sistem Fuzzy'),
    ('Pembelajaran Mesin','Pembelajaran Mesin'),
    ('Pembelajaran Mendalam','Pembelajaran Mendalam'),
    ('Sains Data','Sains Data')
)

    DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Sunday', 'Sunday'),
)

    CLASSSTARTTIME = (
        ('08:00','08:00'),
        ('09:00','09:00'),
        ('10:00','10:00'),
        ('11:00','11:00'),
        ('12:00','12:00'),
        ('13:00','13:00'),
        ('14:00','14:00'),
        ('15:00','15:00'),
        ('16:00','16:00'),
        ('17:00','17:00'),
    )
    CLASSENDTIME = (
        ('08:00','08:00'),
        ('09:00','09:00'),
        ('10:00','10:00'),
        ('11:00','11:00'),
        ('12:00','12:00'),
        ('13:00','13:00'),
        ('14:00','14:00'),
        ('15:00','15:00'),
        ('16:00','16:00'),
        ('17:00','17:00'),
    )

    name = models.CharField(max_length=200, null=True, blank=True)
    matricno = models.CharField(max_length=200, null=True)
    program = models.CharField(max_length=200, null=True, choices=PROGRAM)
    year = models.CharField(max_length=200, null=True, choices=YEAR)
    semester = models.IntegerField(null=True, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    section = models.IntegerField(null=True, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    #section = models.CharField(max_length=200, null=True, choices=SECTION)
    profile_pic = models.ImageField(upload_to=student_directory_path,null=True, blank=True)
    #subjects = models.ForeignKey(Subject,blank=True, null=True, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=200, null=True, choices=SUBJECT)
    #subjects = models.ManyToManyField(Subject)
    #classday = models.CharField(max_length=200, null=True, choices=DAYS_OF_WEEK)
    #classstart = models.CharField(max_length=200, null=True, choices=CLASSSTARTTIME)
    #classend = models.CharField(max_length=200, null=True, choices=CLASSENDTIME)

    #subject = models.ForeignKey(Subject,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.matricno + " " + self.name + " Subject: " + self.subjects) 

class SubjectAssign(models.Model):
    #subname = models.CharField(max_length=50, choices=SUBJECT)
    subname = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subname)

class Time(models.Model):
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK, default='Monday')
    start = models.CharField(max_length=50, choices=CLASSSTARTTIME, default='08:00 am')
    end = models.CharField(max_length=50, choices=CLASSENDTIME, default='10:00 pm')
    student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.day + " " + self.start + " " + self.end)

    """ BRANCH = (
        ('CSE','CSE'),
        ('IT','IT'),
        ('ECE','ECE'),
        ('CHEM','CHEM'),
        ('MECH','MECH'),
        ('EEE','EEE'),
    )
    YEAR = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    SECTION = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
    )

    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    registration_id = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=100, null=True, choices=BRANCH)
    year = models.CharField(max_length=100, null=True, choices=YEAR)
    section = models.CharField(max_length=100, null=True, choices=SECTION)
    profile_pic = models.ImageField(upload_to=student_directory_path ,null=True, blank=True)


    def __str__(self):
        return str(self.registration_id) """

class Attendence(models.Model):

    
    # faculty = models.ForeignKey(Faculty, null = True, on_delete= models.SET_NULL)
    # student = models.ForeignKey(Student, null = True, on_delete= models.SET_NULL)
    user = models.OneToOneField(User, null = True, blank = True, on_delete= models.CASCADE)
    Faculty_Name = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    matricno = models.CharField(max_length=200, null=True, blank=True)
    #date = models.DateField(auto_now_add = True, null = True)
    #date = models.DateField(default=datetime.now)
    date = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    semester = models.CharField(max_length=200, null = True)
    program = models.CharField(max_length=200, null = True)
    subjects = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=200, null = True)
    section = models.CharField(max_length=200, null = True)
    classday = models.CharField(max_length=200, null=True, blank=True)
    classstart = models.CharField(max_length=200, null=True, blank=True)
    classend = models.CharField(max_length=200, null=True, blank=True)
    #classstarttime = models.CharField(max_length=200, null = True, blank=True)
    #classendtime = models.CharField(max_length=200, null = True, blank=True)
    status = models.CharField(max_length=200, null = True, default='Absent')

    def __str__(self):
        return str(self.matricno + " " + self.name)