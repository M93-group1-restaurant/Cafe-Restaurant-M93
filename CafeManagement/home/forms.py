from django import forms
from .models import *

class SignUpForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'required':'true'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name', 'required':'true'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name', 'required':'true'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password', 'required':'true'}))