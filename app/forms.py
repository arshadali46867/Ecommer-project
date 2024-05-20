from django import forms

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from . models import *



class CustomerRegistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','password')



class CustomerProfileForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    locality=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    city=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    zipcode=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    # state=forms.CharField(widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model=CustomerProfileModel
        fields=('name','locality','city','mobile','zipcode','state')
        widgets={'state':forms.Select(attrs={'class':'form-control'})}



class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
           
        

class MyPasswordResetForm(PasswordChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
           