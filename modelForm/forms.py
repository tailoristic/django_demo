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

#  ! Selecting field
class StudenSelectRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        # fields = '__all__' TO GET ALL THE FIELDS IN ORDER SET BY MODEL CLAS
        # exclude = ['name']  TO REMOVE FIELDS WHICH WE DONT NEED IN OUR FORM
        # exclude = ('name',) TUPLE