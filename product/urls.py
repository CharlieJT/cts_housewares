from django.contrib import admin
from django.urls import path, include
from .views import all_products, product

urlpatterns = [
    path('', all_products, name="all_products"),
    path('<int:id>/', product, name="product"),
]
