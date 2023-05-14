from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter Password"}
        )
    )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
