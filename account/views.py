from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.views import home_page
from .forms import UserLoginForm, UserRegistrationForm
from checkout.models import Order, OrderLineItem
from django.db.models import Sum, F

# Create your views here.
@login_required
def logout(request):
    """ This is view used to log the user out when they are logged in """

    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
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
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('home_page'))
            else:
                login_form.add_error(None, "Invalid login credidentials")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", { "login_form": login_form })


def registration(request):
    """ Returns a registration page allowing the user to register for a login account """

    if request.user.is_authenticated:
        return redirect(reverse('home_page'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered & have logged in")
                return redirect(reverse('home_page'))
            else:
                messages.error(request, "Unable to register account")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {"registration_form": registration_form})

@login_required
def user_profile(request):
    """ This is where the user's profile will show with all of the user's details """
    orders = Order.objects.filter(user_id=request.user)
    user = User.objects.get(email=request.user.email)

    for order in orders:
        order_total_price = 0
        for order_item in order.orderlineitem_set.all():
            order_total_price = order_total_price + (order_item.price * order_item.quantity)
        order.total = order_total_price
        

    return render(request, "profile.html", { "profile": user, "orders": orders })
