from django.shortcuts import render
from .models import *
from .forms import *
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
def teacher(request):
    teacher=Teacher.objects.all()
    context={
        'teacher':teacher
    } 
    return render(request, 'teacher.html', context)

def studentform(request):
    context={}
    if request.method == 'POST': # this checks for button click
        form = StudentForm(request.POST)
        if form.is_valid():
            context=""
            for name, value in form.cleaned_data.items():
                print('{}:({} {}' .format\
                    (name, type(value), value))
        #save data locally butnot to the datadbase yet
        request = form.save (commit=False)

        #save each field local varible
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        middlename = form.cleaned_data['middlename']
        grade = form.cleaned_data['grade']
        request.save()# save to the database
    else:# if theyt have not pre4ssed abutton, let them view a blank form
        form = StudentForm()
    # returns the form and all of its fields in the place of contect variables and list
    return render(request , "studentform.html", \
        {'method': request.method, "form":form})

def teacherform(request):
    context={}
    if request.method == 'POST': # this checks for button click
        form = TeacherForm(request.POST)
        if form.is_valid():
            context=""
            for name, value in form.cleaned_data.items():
                print('{}:({} {}' .format\
                    (name, type(value), value))
        #save data locally butnot to the datadbase yet
        request = form.save (commit=False)

        #save each field local varible
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        classtype = form.cleaned_data['classtype']
        roomnumber = form.cleaned_data['roomnumber']
        request.save()# save to the database
    else:# if they have not pre4ssed abutton, let them view a blank form
        form = TeacherForm()
    # returns the form and all of its fields in the place of contect variables and list
    return render(request , "teacherform.html", \
        {'method': request.method, "form":form})