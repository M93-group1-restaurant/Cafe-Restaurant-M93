from django import forms
from .models import *

class SignUpForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'required':'true'}))