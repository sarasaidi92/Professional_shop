from django.shortcuts import render
from django.http import HttpResponse
from .models import Basic

def index(request):
    basics = Basic.objects.all()[0]
    return render(request, template_name= 'index.html', context={'basics':basics})

def about(request):
    return render(request, template_name= 'about.html')