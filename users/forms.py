from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=64, label='Username', widget=forms.TextInput(attrs={'class' : 'form-control mb-2 bg-light', 'placeholder' : 'Username', 'max_length' : '64', 'autocomplete' : "off"}))
    password1 = forms.CharField(max_length=128, label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control mb-2 bg-light', 'placeholder' : 'Password', 'max_length' : '128', 'autocomplete' : "off"}))
    password2 = forms.CharField(max_length=128, label='Repeat password', widget=forms.PasswordInput(attrs={'class' : 'form-control mb-3 bg-light', 'placeholder' : 'Password again', 'max_length' : '128', 'autocomplete' : "off"}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=64, label='Username', widget=forms.TextInput(attrs={'class' : 'form-control mb-2 bg-light', 'placeholder' : 'Username', 'max_length' : '64', 'autocomplete' : "off"}))
    password = forms.CharField(max_length=128, label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control mb-2 bg-light', 'placeholder' : 'Password', 'max_length' : '128', 'autocomplete' : "off"}))