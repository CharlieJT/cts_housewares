from django.shortcuts import render
from product.models import Product
from django.db.models import Q

# Create your views here.
def search_products(request):
    """ This is responsible for searching for products querying on item number, description & about product fields in product database """
    query = request.GET.get('q')
    products = Product.objects.filter(Q(item_number__icontains=query) |
                                    Q(description__icontains=query) |
                                    Q(about_product__icontains=query))

    return render(request, "products.html", {'products': products})