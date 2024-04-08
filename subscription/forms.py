from django import forms
from .models import Subscription


class SubscribeForm(forms.ModelForm):
    """
    Form for subscribing newsletter.
    """

    class Meta:
        model = Subscription
        fields = [
            "email",
        ]