from django import forms
from .models import *

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','science','teacher']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name','last_name','age','speciality']

class ScienceForm(forms.ModelForm):
    class Meta:
        model = Science
        fields = ['name','teacher','cost']