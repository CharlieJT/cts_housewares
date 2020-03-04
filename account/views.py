from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from home.views import home_page

# Create your views here.
def logout(request):
    """This is view used to log the user out when they are logged in"""
    auth.logout(request)
    return redirect(reverse('home_page'))