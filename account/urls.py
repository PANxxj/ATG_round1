from .views import *
from django.urls import path
urlpatterns = [
    path('',signUp,name='signup'),
    path('login',logIn,name='login'),
    # path('dashboard',dashboard,name='signup'),
]
