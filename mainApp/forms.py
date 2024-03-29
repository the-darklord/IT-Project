from django import forms
from .models import Student, Marks,Announcements
from django.utils.safestring import SafeString

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('id',)
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.Textarea(attrs={'class':'form-control'}),
        }
                
class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = '__all__'
        exclude = ('date','id')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
        }
        
class ChangePasswordForm(forms.Form):
    oldPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    newPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))