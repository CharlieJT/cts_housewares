from django.shortcuts import render, redirect, reverse
from product.models import Product
# Create your views here.
def view_cart(request):
    """ This view the contents of the cart """
    return render(request, "cart.html")

def add_to_cart(request, id):
    """ This will add a specific product to the basket """
    quantity=int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart

    return redirect(reverse('home_page'))

def adjust_cart(request, id):
    """ This will adjust the cart of a specific product in the basket """
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    cart[id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, id):
    """ This will remove an item from the basket with a specific id """
    cart = request.session.get('cart', {})
    cart.pop(str(id))
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))