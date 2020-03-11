from django.shortcuts import render
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def all_products(request):

    products = Product.objects.all()
    
    paginator = Paginator(products, 9)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "products.html", {"products": products})
