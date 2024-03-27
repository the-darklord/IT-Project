from django import forms
from .models import Student, Marks,Announcements
from django.utils.safestring import SafeString

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.Textarea(attrs={'class':'form-control'}),
        }
        
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'
        widgets = {
            'student' : forms.Select(attrs={'class':'form-control'}),
            'subject1' : forms.TextInput(attrs={'class':'form-control'}),
            'marks1' : forms.NumberInput(attrs={'class':'form-control'}),
            'subject2' : forms.TextInput(attrs={'class':'form-control'}),
            'marks2' : forms.NumberInput(attrs={'class':'form-control'}),
            'subject3' : forms.TextInput(attrs={'class':'form-control'}),
            'marks3' : forms.NumberInput(attrs={'class':'form-control'}),
        }
        
class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = '__all__'
        exclude = ('date',)
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
        }
        
class ChangePasswordForm(forms.Form):
    oldPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    newPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))