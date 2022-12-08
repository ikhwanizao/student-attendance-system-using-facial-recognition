from django.contrib import admin

from .models import *

# Register your models here.
class SubjectTabularInline(admin.TabularInline):
    model = SubjectAssign
    extra = 0
class TimeTabularInline(admin.TabularInline):
    model = Time
    extra = 0
class StudentAdmin(admin.ModelAdmin):
    inlines = [TimeTabularInline,SubjectTabularInline]
    class Meta: 
        model = Student

admin.site.register(Subject)
admin.site.register(Time)
admin.site.register(Faculty)
admin.site.register(Student, StudentAdmin)
admin.site.register(Attendence)
