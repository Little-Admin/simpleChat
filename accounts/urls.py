from django.urls import path
from accounts import views

urlpatterns = [
    path('sign-up/', views.account_signup, name='Sign-Up'),
    path('login/', views.account_login, name='Login'),
    path('logout/', views.account_logout, name='Logout'),
    path('settings/', views.account_settings, name='settings'),
]