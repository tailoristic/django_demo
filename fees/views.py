from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def my_fun(request):
    return HttpResponse('<h1>Hello fees</h1>')
