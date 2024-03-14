from django import forms
from .models import Student, Marks,Announcements

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'
        
class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = '__all__'
        exclude = ('date',)