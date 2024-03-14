from django.contrib import admin
from .models import Student,Marks,AdminCredentials,StudentCredentials,Announcements
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','password','phone','address']

class MarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject1','marks1','subject2','marks2','subject3','marks3']

class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['title','description','date']

class AdminCredentialsAdmin(admin.ModelAdmin):
    list_display = ['email','password','salt']
    
class StudentCredentialsAdmin(admin.ModelAdmin):
    list_display = ['email','password','salt']

admin.site.register(Student,StudentAdmin)
admin.site.register(Marks,MarksAdmin)
admin.site.register(AdminCredentials,AdminCredentialsAdmin)
admin.site.register(StudentCredentials,StudentCredentialsAdmin)
admin.site.register(Announcements,AnnouncementsAdmin)