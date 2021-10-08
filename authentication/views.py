from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group


def sign_up(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
            messages.success(request, 'Account Created.')
    else:
        fm = RegistrationForm()

    return render(request, 'authentication/signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(
                request=request, data=request.POST)  # NOTE HERE
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=uname, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successful')
                    return HttpResponseRedirect('/authentication/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'authentication/user_login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/authentication/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'authentication/home_page.html', {'name': request.user, 'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/authentication/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/authentication/login/')


def changePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/authentication/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
            return render(request, 'authentication/change_password.html', {'form': fm})
    else:
        return HttpResponseRedirect('/authentication/login/')


def changePassword1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/authentication/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
            return render(request, 'authentication/changePass1.html', {'form': fm})
    else:
        return HttpResponseRedirect('/authentication/login/')


def user_details(request, id):
    if request.user.is_authenticated:
        dt = User.objects.get(pk=id)
        fm = EditUserProfileForm(instance=dt)
        return render(request, 'authentication/user_detail.html', {'form': fm})
    else:
        return HttpResponseRedirect('/authentication/login/')

#  PERMISSIONS AND AUTH


def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'authentication/home_page.html', {'user': request.user})

    else:
        return HttpResponseRedirect('/authentication/login/')
