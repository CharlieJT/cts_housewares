from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from home.views import home_page
from account.forms import UserLoginForm

# Create your views here.
@login_required
def logout(request):
    """ This is view used to log the user out when they are logged in """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('home_page'))


def login(request):
    """ Returns a login page allowing the user to enter their login credentials """
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))

    login_form = UserLoginForm()

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('home_page'))
            else:
                login_form.add_error(None, "Invalid login credidentials")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", { "login_form": login_form })


def registration(request):
    """ Returns a registration page allowing the user to register for a login account """
    return render(request, 'registration.html')