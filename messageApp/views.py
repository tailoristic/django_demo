from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.contrib import messages


def msg_view(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            print(messages.get_level(request))
            messages.add_message(request,messages.SUCCESS, 'Your account has been created')
            messages.success(request,'LEET')
            messages.info(request,'LEET')
            messages.set_level(request,10)
            messages.debug(request,'im Debug')
            messages.error(request,'LEET')
    else:
        fm = StudentRegistration()
            
    context = {'form': fm}
    return render(request, 'messageApp/stud_regis.html', context)
