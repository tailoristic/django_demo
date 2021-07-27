from django import forms
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
    roll = forms.IntegerField(min_value=5)
    def clean_name(self):
        cleanName = self.cleaned_data['name']
        if len(cleanName) < 5:
            raise forms.ValidationError('Enter more than or equal 5 char')
        
        return cleanName
    #  FOR ALL FORM VALIDATION AT ONCE
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valName = self.cleaned_data.get('name')
    #     if len(valName) < 3:
    #         raise forms.ValidationError('Error')
        
    #     valRoll = self.cleaned_data['roll']
    #     if valRoll < 10:
    #         raise forms.ValidationError('Value <= 10')
            