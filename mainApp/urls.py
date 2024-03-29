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
    path('adminHome/manageStudents/update/<int:id>',views.updateStudent,name='updateStudent'),
    path('adminHome/manageStudents/delete/<int:id>',views.deleteStudent,name='deleteStudent'),
    path('adminHome/manageMarks',views.manageMarks,name='manageMarks'),
    path('adminHome/manageMarks/update/<int:id>',views.updateMarks,name='updateMarks'),
    path('adminHome/addAnnouncement',views.addAnnouncement,name='addAnnouncement'),
    path('adminHome/manageAnnouncements',views.manageAnnouncements,name='manageAnnouncements'),
    path('adminHome/manageAnnouncements/update/<int:id>',views.updateAnnouncement,name='updateAnnouncement'),
    path('adminHome/manageAnnouncements/delete/<int:id>',views.deleteAnnouncement,name='deleteAnnouncement'),
]
