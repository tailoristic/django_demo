from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.


def modelForm(request):
    if request.method == 'POST':
        # Update data with instance
        pi = User.objects.get(pk=1)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            # name = fm.cleaned_data['name']
            # email = fm.cleaned_data['email']
            # password = fm.cleaned_data['password']
            # ? Always user cleaned_data to insert into User model Object
            # reg = User(name=name,email=email,password=password)
            # reg.save()
            #  Uncomment ^ only if instance is not used
            fm.save()

    else:
        fm = StudentRegistration()

    context = {'form': fm}
    return render(request, 'modelForm/model_form.html', context)
