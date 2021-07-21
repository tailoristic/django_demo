from django.shortcuts import render
from .forms import StudentRegistration 
# Create your views here.
def studRegistration(request):
    # form = StudentRegistration(auto_id='some_%s')
    # form = StudentRegistration(auto_id=True)
    # form = StudentRegistration(auto_id=False)
    # form = StudentRegistration(auto_id=True, label_suffix=' ')

    form = StudentRegistration(auto_id=True, label_suffix=' ', initial={'name':'Kevin'})
    
    # ORDERING FORM FIELD
    # form.order_fields(field_order=['email','name'])
    
    
    context = {'form':form}
    return render(request,'formApp/registration.html',context)

def formRendering(request):
    form = StudentRegistration()
    context = {'form':form}   
    return render(request,'formApp/registration.html',context)