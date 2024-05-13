from re import M
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= ['firstname', 'lastname', 'middlename','grade','profile_pic']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields= ['firstname', 'lastname', 'classtype','roomnumber']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields=['username','email', 'password1','password2']