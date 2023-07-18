from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign-up/', views.account_signup, name='Sign-Up'),
    path('login/', views.account_login, name='Login'),
    path('logout/', views.account_logout, name='Logout'),
    path('settings/', views.account_settings, name='settings'),
    path('reset_password/', views.passwordResetView.as_view(), name='password_reset'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='passwordResetDone'),
    path('reset_password_confirm/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView, name='password_reset_complete')
]