from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from django.utils.crypto import get_random_string
from Cart.models import *
from .forms import *
from django.views.decorators.http import require_POST
from django.utils import timezone


def order_detail(request,id):
    order = Order.objects.get(id = id)
    form = CouponForm()
    return render(request,'order.html',{'order':order,'form':form})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            code = get_random_string(length=8)
            order = Order.objects.create(user_id=request.user.id,f_name=data['f_name'],l_name=data['l_name'],email=data['email'],address=data['address'],code=code)
            cart = Cart.objects.filter(user_id=request.user.id)
            for c in cart:
                OrderItem.objects.create(user_id=request.user.id,order_id=order.id,product_id=c.product.id,quantity=c.quantity)
            messages.success(request,'submit order successfully','success')
            return redirect('order:order_detail',order.id)

@require_POST
def coupon(request,order_id):
    form = CouponForm(request.POST)
    time = timezone.now()
    if form.is_valid():
        data = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=data,start__lte=time,end__gte=time,active=True)
        except Coupon.DoesNotExist:
            messages.error(request,'code is wrong','danger')
            return redirect('order:order_detail',order_id)
        order = Order.objects.get(id = order_id)
        order.discount = coupon.discount
        order.save()
    return redirect('order:order_detail',order_id)

