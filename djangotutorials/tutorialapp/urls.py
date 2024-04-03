from django.urls import path, imclude
from . import views

urlpatterns = [
    path('base/', views.base, name='base')
]
