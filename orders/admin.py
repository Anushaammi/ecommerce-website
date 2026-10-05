

# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'full_name', 'status', 'total_amount', 'created_at')
    list_filter = ('status',)

admin.site.register(Order, OrderAdmin)