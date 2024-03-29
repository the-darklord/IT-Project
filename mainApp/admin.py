from django.contrib import admin
from .models import Student,Marks,AdminCredentials,StudentCredentials,Announcements
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','phone','address']

class MarksAdmin(admin.ModelAdmin):
    list_display = ['id','student','marks1','marks2','marks3']

class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','date']

class AdminCredentialsAdmin(admin.ModelAdmin):
    list_display = ['id','email','password','salt']
    
class StudentCredentialsAdmin(admin.ModelAdmin):
    list_display = ['id','email','password','salt']

admin.site.register(Student,StudentAdmin)
admin.site.register(Marks,MarksAdmin)
admin.site.register(AdminCredentials,AdminCredentialsAdmin)
admin.site.register(StudentCredentials,StudentCredentialsAdmin)
admin.site.register(Announcements,AnnouncementsAdmin)