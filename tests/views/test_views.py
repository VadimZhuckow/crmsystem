import pytest
from django.urls import reverse
from orders.models.order import Order

@pytest.mark.django_db
def test_order_list(client):
    Order.objects.create(
        table_number=1,
        items=[{'name': 'Item 1', 'price': 50}, {'name': 'Item 2', 'price': 50}],
        total_price=0
    )
    Order.objects.create(
        table_number=2,
        items=[{'name': 'Item 1', 'price': 50}, {'name': 'Item 2', 'price': 50}],
        total_price=0
    )
    response = client.get(reverse('order_list'))
    print(response.context['orders'])
    assert response.status_code == 200
    assert 'orders' in response.context
    assert len(response.context['orders']) == 2  
    assert response.context['orders'][0].total_price == 100
      