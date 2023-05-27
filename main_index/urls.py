from django.urls import path
from main_index import views

urlpatterns = [
    path('', views.index, name='index')
]