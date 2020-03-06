from django.contrib import admin
from django.urls import path, include
from .views import all_products
from django.views import static
from cts_housewares.settings import MEDIA_ROOT

urlpatterns = [
    path('', all_products, name="all_products"),
    path('media/<path>', static.serve, {'document_root': MEDIA_ROOT}),
]
