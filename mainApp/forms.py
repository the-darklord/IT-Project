from django import forms
from .models import Student, Marks

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'