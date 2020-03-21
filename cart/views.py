from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from product.models import Product

# Create your views here.
def view_cart(request):
    """ This view the contents of the cart """
    cart = request.session.get('cart', {})
    
    return render(request, "cart.html")

def add_to_cart(request, id):
    """ This will add a specific product to the basket """
    quantity=int(request.POST.get('quantity'))
    
    product = get_object_or_404(Product, pk=id)
    id = str(id)

    cart = request.session.get('cart', {})
    if cart.get(id, None):
        if cart[id] + quantity > product.stock:
            messages.error(request, "Unable to add an extra '{}' of this item to your cart as it will exceed the number of stock!".format(quantity)) 
        else:
            cart[id] = int(cart[id]) + quantity
            messages.success(request, "Added '{}' extra item(s) of '{}' to your cart!".format(quantity, product.description)) 
    else:
        cart[id] = cart.get(id, quantity)
        messages.success(request, "Added '{}' item(s) of '{}' to your cart!".format(quantity, product.description))

    request.session['cart'] = cart
    
    return redirect(request.META['HTTP_REFERER'])

def adjust_cart(request, id):
    """ This will adjust the cart of a specific product in the cart """
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=id)

    cart[id] = quantity

    request.session['cart'] = cart
    messages.success(request, "Adjusted item '{}' quantity to '{}'!".format(product.description, quantity))

    return redirect(reverse('view_cart'))

def remove_from_cart(request, id):
    """ This will remove an item from the basket with a specific id """
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=id)
    cart.pop(str(id))
    request.session['cart'] = cart
    messages.success(request, "Item '{}' has been removed from your cart!".format(product.description))
    return redirect(reverse('view_cart'))