from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('', include('products.urls')),
]