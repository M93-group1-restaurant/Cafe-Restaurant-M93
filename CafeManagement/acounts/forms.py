from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("phone_number",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("phone_number",)


class LoginForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
