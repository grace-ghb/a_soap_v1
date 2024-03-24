from django.shortcuts import render

def view_cart(request):
    """
    A view that render the shopping cart contents page
    """
    return render(request, "cart/cart.html")
