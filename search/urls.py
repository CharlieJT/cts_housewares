from django.urls import path
from search.views import search_products

urlpatterns = [
    path("", search_products, name="search")
]