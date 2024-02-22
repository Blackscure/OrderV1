from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/api/v1/order/', include('orders.api.urls')),
    path('apps/api/v1/customers/', include('customers.api.urls')),
]
