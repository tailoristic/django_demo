from django.shortcuts import render

# Create your views here.
def master_index(request):
    return render(request,'temp/master_index.html',{'Title':'Template Inheritance'})

def home_page(request):
    return render(request,'temp/home_page.html',{'Title':'Home Page'})

def about_page(request):
    return render(request,'temp/about.html',{'Title':'About Page'})