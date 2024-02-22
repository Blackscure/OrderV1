from django.urls import path

from orders.api.views import OrderView


urlpatterns = [
    path('orders/', OrderView.as_view(), name='order-list'),
]
