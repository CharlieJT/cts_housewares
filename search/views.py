from django.shortcuts import render
from product.models import Product
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count

# Create your views here.
def search_products(request):
    """ This is responsible for searching for products querying on item number, description & about product fields in product database """
    if request.GET:
        query = request.GET.get('q', '')
        products = Product.objects.filter(Q(item_number__icontains=query) |
                                        Q(brand__icontains=query) |
                                        Q(description__icontains=query) |
                                        Q(about_product__icontains=query))

        product_count = products.count()

        page_request_var = "q={}&".format(query)
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
            "page_request_var": page_request_var, 
            "product_count": product_count, 
            "query": query 
        }
        

    return render(request, "products.html", content)