from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
        
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject1 = models.CharField(max_length=100)
    marks1 = models.IntegerField()
    subject2 = models.CharField(max_length=100)
    marks2 = models.IntegerField()
    subject3 = models.CharField(max_length=100)
    marks3 = models.IntegerField()
    
class AdminCredentials(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    
class StudentCredentials(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)