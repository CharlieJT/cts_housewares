from django.contrib import admin
from django.urls import path, include
from .views import logout, login, registration, user_profile, orders
from account import url_reset

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('orders/', orders, name="orders"),
    path('register/', registration, name="registration"),
    path('profile/', user_profile, name="profile"),
    path('password-reset/', include(url_reset))
]