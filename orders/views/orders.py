import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from orders.models.order import Order
from orders.forms.orders import OrderForm

def order_list(request):
    orders = Order.objects.all().order_by('id')
    return render(request, 'orders/order_list.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            items_json = request.POST.get('items')
            items = json.loads(items_json) 
            total_price = sum(item.get('price', 0) for item in items)
            order.total_price = total_price
            order.save()
            return redirect('order_list')
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
