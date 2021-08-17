from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration

# Create your views here.


def student_form(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegistration()

    return render(request, 'model_inheritance/student.html', {'form': fm})


def teacher_form(request):
    if request.method == 'POST':
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = TeacherRegistration()

    return render(request, 'model_inheritance/teacher.html', {'form': fm})
