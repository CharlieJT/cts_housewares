from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def all_products(request):
    """ This will return all of the products & only bring back 12 items on which ever page that you're on """

    brand = request.GET.get('brand', '')
    if brand:
        products = Product.objects.filter(Q(brand__icontains=brand))
        page_request_var = "brand={}&".format(brand)
    else:
        products = Product.objects.all()
        page_request_var = ''
    
    brand_list = Product.objects.values('brand').distinct()
    product_count = products.count()
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    content = { 
        "products": products, 
        "product_count": product_count, 
        "page_request_var": page_request_var,
        "brand": brand,
        "brand_list": brand_list
    }

    return render(request, "products.html", content)


def product(request, id):
    """ This will return a product from the product list with a specific id """
    product = get_object_or_404(Product, pk=id)

    return render(request, "product.html", { "product": product })

