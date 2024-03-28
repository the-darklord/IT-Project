from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    def __str__(self):
        return f"{self.name}"
        
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks1 = models.IntegerField()
    marks2 = models.IntegerField()
    marks3 = models.IntegerField()

class Announcements(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    class Meta:
        ordering = ['-date']

class AdminCredentials(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    
class StudentCredentials(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
