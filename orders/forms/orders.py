from django.forms import forms
from models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        field = [
            'table_number',
            'items',
        ]