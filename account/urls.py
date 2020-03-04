from django.contrib import admin
from django.urls import path, include
from .views import logout, login, registration

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
]