from django.shortcuts import render, get_object_or_404, redirect
from .forms import SubscribeForm
from .models import Subscription
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def subscribe(request):
    """
    Subscription functionality for newsletter
    """
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            messages.info(request, "You have subscribed to our newsletter! Thank you.")
            email = request.POST.get("email")
            subject = "Thank you for Subscribing!"
            message = (
                "Thank you for subscribing to our newsletter,"
                + " you will get latest updates on our new products and deals in upcoming email!"
                + " or you can visit our website at"
                + " https://#.herokuapp.com/"

            )
            from_email = "admin@asoap.com"
            recipient_list = [subscription.email]
            send_mail(subject,
                      message, from_email, recipient_list, fail_silently=False)
            return redirect("/")
    else:
        form = SubcribeForm()

    context = {"form": form}
    return render(request, "index.html", context)