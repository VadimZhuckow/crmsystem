import json

from django.shortcuts import render, redirect
from orders.models.order import Order
from orders.forms.orders import OrderForm

def order_list(request):
    orders = Order.objects.all().order_by('id')
    return render(request, 'orders/order_list.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        table_number = request.POST.get('table_number')
        items = request.POST.get('items')
        status = request.POST.get('status')
        try:
            items = json.loads(items)
            total_price = sum(item['price'] for item in items)
            order = Order(table_number=table_number, items=items, total_price=total_price, status=status)
            order.save()
            return redirect('order_list')
        except Exception as e:
            print(f"Ошибка: {e}")  
    return render(request, 'orders/add_order.html')

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('order_list')

def update_order_status(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.save()
        return redirect('order_list')
    return render(request, 'orders/update_order_status.html', {'order': order})
