from django.shortcuts import render
from .models import Banner

# Create your views here.
def home_page(request):
    """ This will return the home page """
    banners = Banner.objects.all()

    return render(request, "index.html", { "banners": banners })