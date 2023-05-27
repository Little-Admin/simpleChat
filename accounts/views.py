from django.shortcuts import render, redirect
from .forms import Sign_upForm, LoginForm, NewUsernameForm, NewEmailForm, NewPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from calendar import month_name

# Create your views here.
def account_signup(request):
    form = Sign_upForm()

    if request.method == 'POST':
        form = Sign_upForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat_index')

    return render(request, 'startAccount.html', {
        'action' : 'Sign-Up',
        'redirect_to' : 'Login',
        'form' : form
    })

def account_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = request.POST['username'], password = request.POST['password'])
            try:
                login(request, user)
            except AttributeError:
                messages.error(request, 'User or Password are incorrect')
                return redirect('Login')

            return redirect('chat_index')
        
    return render(request, 'startAccount.html', {
        'action' : 'Login',
        'redirect_to' : 'Sign-Up',
        'form' : form
    })

def account_logout(request):
    logout(request)
    return redirect('index')

def account_settings(request):
    # Basic info
    username = request.user.username
    useremail = request.user.email
    last_login = request.user.last_login
    month = last_login.month
    last_login = f"%s/{month_name[int(month)]}/%s" % (last_login.day, last_login.year)
    
    # Forms
    usernameForm = NewUsernameForm()
    emailForm = NewEmailForm()
    passwordForm = NewPasswordForm()

    usernameForm_visibility = False
    emailForm_visibility = False
    passwordForm_visibility = False
    
    if request.method == 'POST':
        match request.POST['formName']:
            case 'username':
                usernameForm = NewUsernameForm(request.POST)
                if usernameForm.is_valid():
                    usernameForm_visibility = False
                    username = usernameForm.cleaned_data['new_username']
                    usernameForm.save(request.user.id)
                    messages.success(request, 'Username Changed')
                else:
                    usernameForm_visibility = True

            case 'email':
                emailForm = NewEmailForm(request.POST)
                if emailForm.is_valid():
                    emailForm_visibility = False
                    useremail = NewEmailForm.cleaned_data['new_email']
                    emailForm.save(request.user.id)
                    messages.success(request, 'Email Changed')
                else:
                    emailForm_visibility = True

            case 'password':
                passwordForm = NewPasswordForm(request.POST)
                if passwordForm.is_valid():
                    passwordForm_visibility = False
                    new_password = passwordForm.cleaned_data['new_password']
                    passwordForm.save(request.user.id)

                    #Relogin
                    user = authenticate(username = request.user.username, password = new_password)
                    login(request, user)

                    messages.success(request, 'Password Changed')
                else:
                    passwordForm_visibility = True

    return render(request, 'account_settings.html', {
        'username' : username,
        'useremail' : useremail,
        'last_login' : last_login,
        'usernameForm' : usernameForm,
        'emailForm' : emailForm,
        'passwordForm' : passwordForm,
        'usernameForm_visibility' : usernameForm_visibility,
        'emailForm_visibility' : emailForm_visibility,
        'passwordForm_visibility' : passwordForm_visibility,
    })