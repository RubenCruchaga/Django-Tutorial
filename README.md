# Django-Tutorial

## Step 1: Creat A project
- `django-admin startproject [project name here]`
- `python -m django startproject [project name here]`

## Step 2: Creat a app
- `django-admin startapp [app name here]`
- `python mange.py startapp [app name here]`

## Step 3: Run web server
- cd into the project folder where manage.py is located
- run `python manage.py runserver`

## Step 4: Build Database
- cd into the folder with manage.py
- `python manage.py migrate`

## Steo 5: creat super user
- cd into the folder with manage.py
- `python manage.py createsuperuser`

## Step 6: Add App to Aetting, Installed App's Dicictionary
- `INSTALLED_APPS =`
- `...`
- `[Name of app],`

## Step 7: Add Templates Folder
- `BASE_DIR = Path(__file__).resolve().parent.parent`
- Add template folder inside app folder.

## View Function
```python
def base(request):
    context={


    }
    return(request, 'base.html', context)
```
## Step 8: Add App's Urls.py to project Urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutorialapp.urls'))
]
```

## Step 9: Add App's Urls.py to App's floder
```python
from django.urls import path, imclude
from . import views

urlpatterns = [
    path('base/', views.base, name='base')
]
```
## Inheriting Code from a template
### base.html
```python
{% block content %}

{% endblock %}
```
### Template
```python
{% load static %}

{% include 'base.html' %}
```
## Making Changes to the Database
### Set 1: Saving Changes
```
python manage.py makemigrations
```
### Step 2: Build Changes into the Database
```
python manage.py migrate
```
