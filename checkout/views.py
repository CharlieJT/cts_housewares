from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import stripe
from django.conf import settings
from django.utils import timezone
from product.views import Product
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required
def checkout(request):
    """ 
    This is where you can make a checkout, depending on whether you have entered valid inputs will determind
    whether you make a successful payment
    """

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.user_id = request.user
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                product.stock = product.stock - quantity
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    price=product.price,
                    quantity=quantity
                )
                product.save()
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('successful_payment'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take payment with that card!")
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()

    content =  { 
        'order_form': order_form, 
        'payment_form': payment_form, 
        'publishable': settings.STRIPE_PUBLISHABLE
    }

    return render(request, "checkout.html", content)

@login_required()
def successful_payment(request):
    """ This will return the successful payment page """
    brand_list = Product.objects.values('brand').distinct()

    return render(request, "successful_payment.html", {"brand_list": brand_list})
