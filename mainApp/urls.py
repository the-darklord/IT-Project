from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('studentLogin',views.studentLogin, name='studentLogin'),
    path('adminLogin',views.adminLogin,name='adminLogin'),
    path('studentHome',views.studentHome,name='studentHome'),
    path('adminHome',views.adminHome,name='adminHome'),
    path('logout',views.logout,name='logout'),
    path('changepassword',views.changepassword,name='changepassword'),
]
