from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P0oX405a2XN2ORrcVzlwwXEED0mcV52O7Hxq0D6LjYL55MgoWcjHl55GpyUliKigCb6cBmowWJq2ehpwCtrrxTe00eZCfzkPh',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)