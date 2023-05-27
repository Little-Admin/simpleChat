from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Sign_upForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder' : 'email'
    }))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder' : 'user name'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password again'
    }))
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {
            'username': None,
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder' : 'user name'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password'
    }))

class NewUsernameForm(forms.Form):
    new_username = forms.CharField(max_length=30)

    class Meta:
        model = User

    def clean(self):
        new_username = self.cleaned_data.get('new_username')
        if User.objects.filter(username=new_username).exists():
            raise ValidationError('User exists')
        
        return self.cleaned_data
    
    def save(self, id):
        user = User.objects.get(id = id)
        user.username = self.cleaned_data.get('new_username')
        user.save()

class NewEmailForm(forms.Form):
    new_email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder' : 'email'
    }))

    def clean(self):
        new_email = self.cleaned_data.get('new_email')
        if User.objects.filter(email=new_email).exists():
            raise ValidationError('Email is in use')

        return self.cleaned_data
    
    def save(self, id):
        user = User.objects.get(id = id)
        user.email = self.cleaned_data.get('new_email')
        user.save()

class NewPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'new password'
    }))
    new_passwordagain = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password again',
    }))

    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password'].label = 'Password'
        self.fields['new_passwordagain'].label = 'Password (again)'

    def clean(self):
        new_password = self.cleaned_data['new_password']
        new_passwordagain = self.cleaned_data['new_passwordagain']

        if new_password != new_passwordagain:
            raise ValidationError('Password does not match')

        return self.cleaned_data
    
    def save(self, id):
        user = User.objects.get(id = id)
        user.set_password(self.cleaned_data['new_password'])
        user.save()