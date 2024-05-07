from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('teacher/', views.teacher, name= 'teacher'),
    path('studentforms/', views.studentform, name= 'studentform'),
    path('teacherforms/', views.teacherform, name= 'teacherform'),
    path('register/', views.register, name = "register"),
    path('profile/', views.profile, name = "profile"),
]