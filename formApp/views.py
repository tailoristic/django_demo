from django.shortcuts import render
from .forms import StudentRegistration, FormField
from django.http import HttpResponseRedirect
from modelApp.models import Student

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

# def formAttrib(request):
    # form = StudentRegistration(initial={'mobile':7096236263})
    # if request.method == 'POST':
    #     fm = StudentRegistration(request.POST)
    #     if fm.is_valid():
    #         print("FORM VALIDATED")
    #         print("NAME",fm.cleaned_data['name'])
    #         print("EMAIL",fm.cleaned_data['email'])
    # form = StudentRegistration()
    # context = {'form':form}   
    # return render(request,'formApp/form_attrib.html',context)
    
def formAttrib(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("FORM VALIDATED")
            print("NAME",fm.cleaned_data['name'])
            print("EMAIL",fm.cleaned_data['email'])
            context = {'name':fm.cleaned_data['name']}
            return HttpResponseRedirect('/success/')
            # return render(request,'formApp/home_page.html',context)
    else:
        fm = StudentRegistration()
    
    context = {'form':fm}   
    return render(request,'formApp/form_attrib.html',context)

def thanks(request):
    context = {'name':Student.objects.all()}
    return render(request, 'formApp/home_page.html',context)

# Build in form inputs
# 
    
def formInputs(request):
    if request.method == 'POST':
        fm = FormField(request.POST)
        if fm.is_valid():
            print("FORM VALIDATED")
            print("NAME",fm.cleaned_data['name'])
            print("NAME",fm.cleaned_data['roll'])
            context = {'name':fm.cleaned_data['name']}
            # return HttpResponseRedirect('/success/')
            # return render(request,'formApp/home_page.html',context)
    else:
        fm = FormField()
    
    context = {'form':fm}   
    return render(request,'formApp/form_inputs.html',context)