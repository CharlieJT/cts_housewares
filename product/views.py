from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def all_products(request):

    products = Product.objects.all()
    product_count = products.count()
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "products.html", { "products": products, "product_count": product_count })

def product(request, id):

    product = get_object_or_404(Product, pk=id)

    return render(request, "product.html", { "product": product })

