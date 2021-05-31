from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# SECRET_KEY = 'django-insecure-*5#v+#!^(y8tcq3)$y@-p98u)0500z^0m+u(f04fcbb5t))+(='
def my_fun(request):
    return HttpResponse('<h1>Hello course insie url course</h1>')

def home(request):
    return render(request,'firstApplication/home.html')