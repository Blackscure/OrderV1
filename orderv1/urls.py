from django.contrib import admin
from django.urls import include, path,url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^oidc/', include('oidc_provider.urls', namespace='oidc_provider')),
    path('apps/api/v1/order/', include('orders.api.urls')),
    path('apps/api/v1/customers/', include('customers.api.urls')),
]
