from django.shortcuts import render
from .models import Student

def modelIndex(request):
    stud = Student.objects.all()
    return render(request,'modelApp/index.html',{'stud':stud})