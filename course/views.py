from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_fun(request):
    return HttpResponse('<h1>Hello course insie url course</h1>')

def home(request):
    return render(request,'firstApplication/home.html')