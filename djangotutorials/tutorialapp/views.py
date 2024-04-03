from django.shortcuts import render

# Create your views here.


def base(request):
    context={


    }
    return(request, 'base.html', context)