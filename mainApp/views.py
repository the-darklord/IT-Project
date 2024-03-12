from django.shortcuts import render,redirect
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
        return render(request, 'mainApp/studentHome.html',{'email':request.session['studentEmail'],'password':request.session['studentPassword']})
    elif request.session.has_key('adminEmail'):
        return redirect('adminHome')
    elif request.method=="POST":
        email = request.POST['typeEmailX']
        password = request.POST['typePasswordX']
        request.session['studentEmail'] = email
        request.session['studentPassword'] = password
        request.session.modified = True
        request.session.save()
        return render(request, 'mainApp/studentHome.html',{'email':email,'password':password})
    else:
        return redirect('studentLogin')
    
def adminHome(request):
    if request.session.has_key('adminEmail'):
        return render(request, 'mainApp/adminHome.html',{'email':request.session['adminEmail'],'password':request.session['adminPassword']})
    elif request.session.has_key('studentEmail'):
        return redirect('studentHome')
    elif request.method=="POST":
        email = request.POST['typeEmailX']
        password = request.POST['typePasswordX']
        request.session['adminEmail'] = email
        request.session['adminPassword'] = password
        request.session.modified = True
        request.session.save()
        return render(request, 'mainApp/adminHome.html',{'email':email,'password':password})
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