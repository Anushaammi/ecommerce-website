from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            full_name=request.POST['full_name'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            total_amount=cart.get_total_price(),
        )
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'],
            )
        cart.clear()
        return redirect('order_success', order_id=order.id)
    return render(request, 'orders/checkout.html', {'cart': cart})

def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_success.html', {'order': order})