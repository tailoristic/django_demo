from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_fun(request):
    # RETURNING HTTP RESPONSE
    return HttpResponse('<h1>Hello course insie url course</h1>')

def home(request):
    # SIMPLE DEMO OF RENDERING HTML TEMPLATE
    return render(request,'home.html')

def dashboard(request):
    # DICTIONARy
    courseName = {'name': 'Github'}
    # PASS IT TO RENDER FUNCTION
    return render(request,'dashboard.html',courseName)