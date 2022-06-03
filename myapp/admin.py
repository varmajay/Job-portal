from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['name','email','role','gender','phone','address','profile']

@admin.register(Jobs)
class AdminJobs(admin.ModelAdmin):
    list_display = ['HR_name','HR_email','categories','type','position','salary','job_description','experience','vacancy','time']
    def HR_name(self, obj):
        return obj.hr.name
    def HR_email(self, obj):
        return obj.hr.email

@admin.register(Application)
class AdminApplication(admin.ModelAdmin):
    list_display = ['name','email','phone','dob','gender','address','resume']

