from django.contrib.auth.decorators import login_required
from cart.models import Cart
from order.forms import OrderForm
from order.models import OrderItem, Order
from django.shortcuts import render

@login_required(login_url='/login/')
def order_create(request):
    cart = Cart(request)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
                order.save()


            for cart_item in cart:
                OrderItem.objects.create(order=order, item=cart_item['item'], price=cart_item['item_price'], quantity=cart_item['quantity'])

            cart.clear()


            return render(request, 'order/created.html', {'order': order})

    else:
        form = OrderForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})


def order_complete(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)
    return render(request, 'order/created.html', {'order':order})
