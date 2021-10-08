from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'}  # <-- For changing default label tags names

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta: 
        model = User
        fields = ['username','first_name','last_name','email', 'date_joined', 'last_login']
        labels = {'email': 'Email'}
        
class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta: 
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}