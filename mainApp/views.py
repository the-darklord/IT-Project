import datetime
import bcrypt

from django.shortcuts import render,redirect
from .models import Student,Marks,AdminCredentials,StudentCredentials,Announcements
from .forms import StudentForm,AnnouncementsForm,ChangePasswordForm
# Create your views here.

def login(request):
    if request.session.has_key('adminEmail'):
        return redirect('adminHome')
    elif request.session.has_key('studentEmail'):
        return redirect('studentHome')
    else:
        return render(request, 'mainApp/login.html')

def studentLogin(request):
    if request.session.has_key('studentEmail'):
        return redirect('studentHome')
    elif request.session.has_key('adminEmail'):
        return redirect('adminHome')
    else:
        return render(request, 'mainApp/studentLogin.html')

def adminLogin(request):
    if request.session.has_key('adminEmail'):
        return redirect('adminHome')
    elif request.session.has_key('studentEmail'):
        return redirect('studentHome')
    else:
        return render(request, 'mainApp/adminLogin.html')

def studentHome(request):
    if request.session.has_key('studentEmail'):
        student = Student.objects.get(email=request.session['studentEmail'])
        try:
            marks = Marks.objects.get(student=student)
        except Marks.DoesNotExist:
            marks = Marks(student=student,marks1=0,marks2=0,marks3=0)
        announcements = Announcements.objects.all()
        return render(request, 'mainApp/studentHome.html',{'student':student,'marks':marks,'announcements':announcements})
    elif request.session.has_key('adminEmail'):
        return redirect('adminHome')
    elif request.method=="POST":
        email = request.POST['typeEmailX']
        password = request.POST['typePasswordX']
        try:
            obj = StudentCredentials.objects.get(email=email)
        except StudentCredentials.DoesNotExist:
            return redirect('studentLogin')
        salt = obj.salt
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'),salt.encode('utf-8'))
        if hashedPassword.decode('utf-8') != obj.password:
            return redirect('studentLogin')
        request.session['studentEmail'] = email
        request.session['studentPassword'] = hashedPassword.decode('utf-8')
        request.session.modified = True
        request.session.save()
        student = Student.objects.get(email=email)
        try:
            marks = Marks.objects.get(student=student)
        except Marks.DoesNotExist:
            marks = Marks(student=student,marks1=0,marks2=0,marks3=0)
        announcements = Announcements.objects.all()
        return render(request, 'mainApp/studentHome.html',{'student':student,'marks':marks,'announcements':announcements})
    else:
        return redirect('studentLogin')
    
def adminHome(request):
    if request.session.has_key('adminEmail'):
        return render(request, 'mainApp/adminHome.html')
    elif request.session.has_key('studentEmail'):
        return redirect('studentHome')
    elif request.method=="POST":
        email = request.POST['typeEmailX']
        password = request.POST['typePasswordX']
        try:
            obj = AdminCredentials.objects.get(email=email)
        except AdminCredentials.DoesNotExist:
            return redirect('adminLogin')
        salt = obj.salt
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'),salt.encode('utf-8'))
        if hashedPassword.decode('utf-8') != obj.password:
            return redirect('adminLogin')
        request.session['adminEmail'] = email
        request.session['adminPassword'] = hashedPassword.decode('utf-8')
        request.session.modified = True
        request.session.save()
        return render(request, 'mainApp/adminHome.html')
    else:
        return redirect('adminLogin')
    
def changepassword(request):
    if request.session.has_key('studentEmail'):
        if request.method=="POST":
            oldPassword = request.POST['oldPassword']
            newPassword = request.POST['newPassword']
            confirmPassword = request.POST['confirmPassword']
            if newPassword != confirmPassword:
                return render(request, 'mainApp/changepassword.html',{'changepasswordform':ChangePasswordForm(),'message':'Passwords do not match'})
            salt = StudentCredentials.objects.get(email=request.session['studentEmail']).salt
            hashedPassword = bcrypt.hashpw(oldPassword.encode('utf-8'),salt.encode('utf-8'))
            if hashedPassword.decode('utf-8') == StudentCredentials.objects.get(email=request.session['studentEmail']).password:
                salt = bcrypt.gensalt()
                hashedPassword = bcrypt.hashpw(newPassword.encode('utf-8'),salt)
                obj = StudentCredentials.objects.get(email=request.session['studentEmail'])
                obj.password = hashedPassword.decode('utf-8')
                obj.salt = salt.decode('utf-8')
                obj.save()
                obj = Student.objects.get(email=request.session['studentEmail'])
                obj.password = newPassword
                obj.save()
                return redirect('studentHome')
            else:
                return render(request, 'mainApp/changepassword.html',{'changepasswordform':ChangePasswordForm(),'message':'Old Password is incorrect'})
        else:
            return render(request, 'mainApp/changepassword.html',{'changepasswordform':ChangePasswordForm(),'message':''})
    elif request.session.has_key('adminEmail'):
        if request.method=="POST":
            oldPassword = request.POST['oldPassword']
            newPassword = request.POST['newPassword']
            confirmPassword = request.POST['confirmPassword']
            if newPassword != confirmPassword:
                return render(request, 'mainApp/changepassword.html',{'changepasswordform':ChangePasswordForm(),'message':'Passwords do not match'})
            salt = AdminCredentials.objects.get(email=request.session['adminEmail']).salt
            hashedPassword = bcrypt.hashpw(oldPassword.encode('utf-8'),salt.encode('utf-8'))
            if hashedPassword.decode('utf-8') == AdminCredentials.objects.get(email=request.session['adminEmail']).password:
                salt = bcrypt.gensalt()
                hashedPassword = bcrypt.hashpw(newPassword.encode('utf-8'),salt)
                obj = AdminCredentials.objects.get(email=request.session['adminEmail'])
                obj.password = hashedPassword.decode('utf-8')
                obj.salt = salt.decode('utf-8')
                obj.save()
                return redirect('adminHome')
            else:
                return render(request, 'mainApp/changepassword.html',{'changepasswordform':ChangePasswordForm(),'message':'Old Password is incorrect'})
        else:
            return render(request, 'mainApp/changepassword.html',{'changepasswordform':ChangePasswordForm(),'message':''})
    else:
        return redirect('login')

def addStudent(request):
    if request.session.has_key('adminEmail'):
        if request.method=="POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                salt = bcrypt.gensalt()
                hashedPassword = bcrypt.hashpw(password.encode('utf-8'),salt)
                obj = StudentCredentials(email=email,password=hashedPassword.decode('utf-8'),salt=salt.decode('utf-8'))
                obj.save()
                obj = Marks(student=Student.objects.get(email=email),marks1=0,marks2=0,marks3=0)
                obj.save()
            return render(request, 'mainApp/addStudent.html',{'studentform':StudentForm()})
        else:
            return render(request, 'mainApp/addStudent.html',{'studentform':StudentForm()})
    else:
        return redirect('login')

def manageStudents(request):
    if request.session.has_key('adminEmail'):
        students = Student.objects.all()
        return render(request, 'mainApp/manageStudents.html',{'student':students})
    else:
        return redirect('login')

def updateStudent(request,id):
    if request.session.has_key('adminEmail'):
        if request.method=="POST":
            student = Student.objects.get(id=id)
            student.name = request.POST['name']
            student.email = request.POST['email']
            student.password = request.POST['password']
            salt = StudentCredentials.objects.get(email=student.email).salt
            hashedPassword = bcrypt.hashpw(student.password.encode('utf-8'),salt.encode('utf-8'))
            obj = StudentCredentials.objects.get(email=student.email)
            obj.password = hashedPassword.decode('utf-8')
            obj.save()            
            student.phone = request.POST['phone']
            student.address = request.POST['address']
            student.save()
            return redirect('manageStudents')
        else:
            student = Student.objects.get(id=id)
            return render(request, 'mainApp/updateStudent.html',{'student':student})
    else:
        return redirect('login')

def deleteStudent(request,id):
    if request.session.has_key('adminEmail'):
        student = Student.objects.get(id=id)
        StudentCredentials.objects.get(email=student.email).delete()
        Marks.objects.get(student=student).delete()
        Student.objects.get(id=id).delete()
        return redirect('manageStudents')
    else:
        return redirect('login')
    
def manageMarks(request):
    if request.session.has_key('adminEmail'):
        marks = Marks.objects.all()
        return render(request, 'mainApp/manageMarks.html',{'marks':marks})
    else:
        return redirect('login')

def updateMarks(request,id):
    if request.session.has_key('adminEmail'):
        if request.method=="POST":
            marks = Marks.objects.get(id=id)
            marks.marks1 = request.POST['marks1']
            marks.marks2 = request.POST['marks2']
            marks.marks3 = request.POST['marks3']
            marks.save()
            return redirect('manageMarks')
        else:
            marks = Marks.objects.get(id=id)
            return render(request, 'mainApp/updateMarks.html',{'marks':marks})
    else:
        return redirect('login')

def addAnnouncement(request):
    if request.session.has_key('adminEmail'):
        if request.method=="POST":
            form = AnnouncementsForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.date = datetime.datetime.now()
                post.save()
            return render(request, 'mainApp/addAnnouncement.html',{'announcementsform':AnnouncementsForm()})
        else:
            return render(request, 'mainApp/addAnnouncement.html',{'announcementsform':AnnouncementsForm()})
    else:
        return redirect('login')

def manageAnnouncements(request):
    if request.session.has_key('adminEmail'):
        announcements = Announcements.objects.all()
        return render(request, 'mainApp/manageAnnouncements.html',{'announcements':announcements})
    else:
        return redirect('login')
    
def updateAnnouncement(request,id):
    if request.session.has_key('adminEmail'):
        if request.method=="POST":
            announcement = Announcements.objects.get(id=id)
            announcement.title = request.POST['title']
            announcement.description = request.POST['description']
            announcement.save()
            return redirect('manageAnnouncements')
        else:
            announcement = Announcements.objects.get(id=id)
            return render(request, 'mainApp/updateAnnouncement.html',{'announcement':announcement})
    else:
        return redirect('login')
    
def deleteAnnouncement(request,id):
    if request.session.has_key('adminEmail'):
        Announcements.objects.get(id=id).delete()
        return redirect('manageAnnouncements')
    else:
        return redirect('login')
    
def logout(request):
    if request.session.has_key('studentEmail'):
        del request.session['studentEmail']
        del request.session['studentPassword']
    if request.session.has_key('adminEmail'):
        del request.session['adminEmail']
        del request.session['adminPassword']
    return redirect('login')