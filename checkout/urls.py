from django.urls import path
from .views import checkout, successful_payment

urlpatterns = [
    path('', checkout, name="checkout"),
    path('successful_payment/', successful_payment, name="successful_payment")
]