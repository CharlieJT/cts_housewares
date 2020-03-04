from django.shortcuts import render

# Create your views here.
def home_page(request):
    """ This will return the home page """
    return render(request, "index.html")