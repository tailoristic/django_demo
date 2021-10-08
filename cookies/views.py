from django.shortcuts import render
from datetime import datetime, timedelta

## SET COOKIES
def setcookies(request):
    response =  render(request, 'cookies/setcookie.html')
    # response.set_cookie('name','Kevin', max_age=60) # <- max_age in seconds
    # response.set_cookie('name','Kevin', expires=datetime.utcnow() + timedelta(days=2))
    response.set_signed_cookie('name','KevinSigned', salt='nm', expires=datetime.utcnow() + timedelta(days=2))
    return response

## GET COOKIES
def getcookies(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    # name = request.COOKIES.get('name', 'Guest') # <- In case if cookie is deleted
    name = request.get_signed_cookie('name',salt='nm') # default = 'Guest'
    return render(request, 'cookies/getcookie.html', {'cookie':name})


## DELETE COOKIES
def delcookies(request):
    response =  render(request, 'cookies/delcookie.html')
    response.delete_cookie('name')
    return response