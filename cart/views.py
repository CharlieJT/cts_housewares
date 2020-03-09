from django.shortcuts import render, redirect, reverse

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

    print(quantity)
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))