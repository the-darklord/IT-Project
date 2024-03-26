import datetime
import bcrypt

from django.shortcuts import render,redirect
from .models import Student,Marks,AdminCredentials,StudentCredentials,Announcements
from .forms import StudentForm,MarksForm,AnnouncementsForm
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
            marks = Marks(student=student,subject1='Subject 1',marks1=0,subject2='Subject 2',marks2=0,subject3='Subject 3',marks3=0)
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
            marks = Marks(student=student,subject1='Subject 1',marks1=0,subject2='Subject 2',marks2=0,subject3='Subject 3',marks3=0)
        announcements = Announcements.objects.all()
        return render(request, 'mainApp/studentHome.html',{'student':student,'marks':marks,'announcements':announcements})
    else:
        return redirect('studentLogin')
    
def adminHome(request):
    if request.session.has_key('adminEmail'):
        student = Student.objects.all()
        marks = Marks.objects.all()
        announcements = Announcements.objects.all()
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            salt = bcrypt.gensalt()
            hashedPassword = bcrypt.hashpw(password.encode('utf-8'),salt)
            obj = StudentCredentials(email=email,password=hashedPassword.decode('utf-8'),salt=salt.decode('utf-8'))
            obj.save()
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
        form = AnnouncementsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = datetime.datetime.now()
            post.save()
        return render(request, 'mainApp/adminHome.html',{'student':student,'marks':marks,'studentform':StudentForm(),'marksform':MarksForm(),'announcementsform':AnnouncementsForm(),'announcements':announcements})
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
        student = Student.objects.all()
        marks = Marks.objects.all()
        announcements = Announcements.objects.all()
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            salt = bcrypt.gensalt()
            hashedPassword = bcrypt.hashpw(password.encode('utf-8'),salt)
            obj = StudentCredentials(email=email,password=hashedPassword.decode('utf-8'),salt=salt.decode('utf-8'))
            obj.save()
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
        form = AnnouncementsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = datetime.datetime.now()
            post.save()
        return render(request, 'mainApp/adminHome.html',{'student':student,'marks':marks,'studentform':StudentForm(),'marksform':MarksForm(),'announcementsform':AnnouncementsForm(),'announcements':announcements})
    else:
        return redirect('adminLogin')
    
def logout(request):
    if request.session.has_key('studentEmail'):
        del request.session['studentEmail']
        del request.session['studentPassword']
    if request.session.has_key('adminEmail'):
        del request.session['adminEmail']
        del request.session['adminPassword']
    return redirect('login')