from django.urls import path
from orders.views.orders import order_list, add_order

urlpatterns = [
    path('', order_list, name='order_list'),
    path('add/', add_order, name='add_order'),
    # path('delete/<int:order_id>/', delete_order, name='delete_order'),
    # path('update/<int:order_id>/', update_order_status, name='update_order_status'),
]