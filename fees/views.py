from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def my_View(request):
    a = 'Kevin'
    return HttpResponse(f'<h1>Hesslslo {a}</h1>')
