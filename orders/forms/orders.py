from django import forms
from orders.models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'table_number',
            'items',
        ]