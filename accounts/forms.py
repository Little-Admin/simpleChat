from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts.models import timeZone, userTimeZone

class Sign_upForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder' : 'email',
        'class' : 'inputW'
    }))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder' : 'user name',
        'class' : 'inputW'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password',
        'class' : 'inputW'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password again',
        'class' : 'inputW'
    }))
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {
            'username': None,
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder' : 'user name',
        'class' : 'inputW'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password',
        'class' : 'inputW'
    }))


# Settings

class NewUsernameForm(forms.Form):
    new_username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder' : 'username',
        'class' : 'inputW'
    }))

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
        'placeholder' : 'email',
        'class' : 'inputW'
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

class ChangePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label= ("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label= ("New password confirmation"),
                                    widget=forms.PasswordInput)

class ChangeTimeZoneForm(forms.Form):
    #Get Choices
    timeZonesChoices = []
    timeZoneObjs = timeZone.objects.all()
    for timeZone in timeZoneObjs:
        timeZonesChoices.append((timeZone, timeZone))


    timeZone = forms.ChoiceField(choices=timeZonesChoices, widget=forms.Select(
        attrs={
            'id' : 'timeZoneSelect'
        }
    ))

    def save(self, id):
        user = User.objects.get(id = id)
        usertz = user.timeZone.get()
        usertz.timeZone = self.cleaned_data['timeZone']
        usertz.save()