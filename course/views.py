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
    courseName = {'name': 'Django'}
    # PASS IT TO RENDER FUNCTION
    return render(request,'dashboard.html',courseName)
def forLoopExample(request):
    myList = {'stud': ["Student 1", "Student 2", "Student 3", "Student 4"]}
    return render(request,'dashboard.html', myList)
  
def nestedForLoop(request):
      stu = {
              'student1':{'name': 'Rahul', 'rollNo': 101},     
              'student2':{'name': 'Rajesh', 'rollNo': 102},
              'student3':{'name': 'Sam', 'rollNo': 103},
              'student4':{'name': 'Jon', 'rollNo': 104},
            },
      students = {'student': stu}
      return render(request,'dashboard.html', students)

