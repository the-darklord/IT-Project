from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('studentLogin',views.studentLogin,name='studentLogin'),
    path('adminLogin/',views.adminLogin,name='adminLogin'),
    path('studentHome',views.studentHome,name='studentHome'),
    path('adminHome',views.adminHome,name='adminHome'),
    path('logout',views.logout,name='logout'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('adminHome/addStudent',views.addStudent,name='addStudent'),
    path('adminHome/manageStudents',views.manageStudents,name='manageStudents'),
    path('adminHome/manageMarks',views.manageMarks,name='manageMarks'),
    path('adminHome/addAnnouncement',views.addAnnouncement,name='addAnnouncement'),
    path('adminHome/manageAnnouncements',views.manageAnnouncements,name='manageAnnouncements'),
]
