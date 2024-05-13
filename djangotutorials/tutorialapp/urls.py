from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
