from django import forms
from django.core.exceptions import ValidationError
from askme.models import *
import re
import pdb

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=4)
    continue_ = forms.CharField(widget=forms.HiddenInput(), initial='index')
   
    
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)
    continue_ = forms.CharField(widget=forms.HiddenInput(), initial='login')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def clean_username(self):
        pattern = r'^[a-zA-Z0-9_]+$'
        data = self.cleaned_data['username']
        
        if not re.match(pattern, data):    
            raise ValidationError('This username is prohibited')
        return data
        
    def clean_first_name(self):
        pattern = r'^[a-zA-Z]+$'
        data = self.cleaned_data['first_name']
        if not re.match(pattern, data):
            raise ValidationError('This first name is prohibited')
    
    def clean_last_name(self):
        pattern = r'^[a-zA-Z]+$'
        data = self.cleaned_data['last_name']
        if not re.match(pattern, data):
            raise ValidationError('This last name is prohibited')
        
    def clean_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        data = self.cleaned_data['email']
        if not re.match(pattern, data):    
            raise ValidationError('Invalid email')
        return data
    
    def clean_password_check(self):
        if not self.cleaned_data['password_check'] == self.cleaned_data['password']:
            raise ValidationError('Passwords are not same')
                
