from django.shortcuts import render
from .models import *
# Create your views here.


def base(request):
    context={

    }

    return render(request, 'base.html', context)

def home(request):
    context={

    }
    
    return render(request, 'home.html', context)

def students(request):
    students=Student.objects.all() # gets all recorded and save students
    context={
        'students':students, # EXPORTS STUDENTS LIST TO THE TEMPLATE(WEBPAGE)
    }

    return render(request,'students.html', context)