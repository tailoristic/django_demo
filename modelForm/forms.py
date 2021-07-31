from django import forms
from django.core import validators
from .models import User


class StudentRegistration(forms.ModelForm):
    # name = forms.CharField(max_length=50, required=False)
    # ! HIGH PRIORTIY

    class Meta:
        model = User    
        fields = ['name', 'email', 'password']
        labels = {
            'name': 'Enter Name'
        }
        help_text = {'name': 'Joe'}
        error_messages = {
            'name': {
                'required': 'Say my name'
            }
        }
        widgets = {
            'password': forms.PasswordInput,
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Name here'})
        }
