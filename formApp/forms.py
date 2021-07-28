from django import forms
from django.core import validators
# 
class StudentRegistration(forms.Form):
    # name = forms.CharField(label="Your Name", label_suffix="", initial="kevin", required=False,disabled=True)
    name = forms.CharField()
    # email = forms.EmailField(help_text="example@email.com")
    # email = forms.EmailField(widget=forms.CheckboxInput)
    # email = forms.EmailField(widget=forms.FileInput)
    email = forms.EmailField()
    # mobile = forms.IntegerField(widget=forms.PasswordInput())
    mobile = forms.IntegerField()
    # key = forms.CharField()
    # key = forms.CharField(widget=forms.HiddenInput())
    
class FormField(forms.Form):
    # min_length=5, max_length=10,
    name = forms.CharField(label_suffix='', error_messages={'min_length':"Minimum length should be more than 1",'required':"Enter your name"})
    roll = forms.IntegerField()
    address = forms.CharField(validators=[validators.MaxLengthValidator(20)])
    password = forms.CharField(widget=forms.PasswordInput)
    rPassword = forms.CharField(widget=forms.PasswordInput, label=('Confirm Password'))
    # def clean_name(self):
    #     cleanName = self.cleaned_data['name']
    #     if len(cleanName) < 5:
    #         raise forms.ValidationError('Enter more than or equal 5 char')
        
    #     return cleanName
    #  FOR ALL FORM VALIDATION AT ONCE
    def clean(self):
        cleaned_data = super().clean()
        valName = self.cleaned_data.get('name')
        valRoll = self.cleaned_data.get('roll')
        valPwd = self.cleaned_data.get('password')
        valRPwd = self.cleaned_data.get('rPassword')
        if valPwd != valRPwd:
            raise forms.ValidationError("Password does not match")
        
        if valName:
            if len(valName) < 4:
                raise forms.ValidationError('Error')
        
        if valRoll:
            if valRoll < 10:
                raise forms.ValidationError('Value <= 10')
        