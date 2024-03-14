import bcrypt

from django.shortcuts import render,redirect
from .models import Student,Marks,AdminCredentials,StudentCredentials
from .forms import StudentForm,MarksForm
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
        marks = Marks.objects.get(student=student)
        return render(request, 'mainApp/studentHome.html',{'student':student,'marks':marks})
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
        marks = Marks.objects.get(student=student)
        return render(request, 'mainApp/studentHome.html',{'student':student,'marks':marks})
    else:
        return redirect('studentLogin')
    
def adminHome(request):
    if request.session.has_key('adminEmail'):
        student = Student.objects.all()
        marks = Marks.objects.all()
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'mainApp/adminHome.html',{'student':student,'marks':marks,'studentform':StudentForm(),'marksform':MarksForm()})
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
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'mainApp/adminHome.html',{'student':student,'marks':marks,'studentform':StudentForm(),'marksform':MarksForm()})
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