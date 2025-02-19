from django.contrib import admin
from orders.models.order import Order


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )