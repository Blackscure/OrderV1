from django.urls import path

from customers.api.views import CustomerView


urlpatterns = [
    path('customers/', CustomerView.as_view(), name='customer'),
]
