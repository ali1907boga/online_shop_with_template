from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from Order.models import *

def cart_detail(request):
    order_form = OrderForm()
    cart = Cart.objects.filter(user_id=request.user.id)
    total = 0
    for c in cart:
        total += c.quantity * c.product.total_price

    return render(request,'cart.html',{'cart':cart,'total':total,'order_form':order_form})

def add_cart(request,id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=id)
    if product.status == 'None':
        data = Cart.objects.filter(user_id=request.user.id,product_id=id)
        if data:
            check = 'yes'
        else:
            check = 'no'
        if request.method == 'POST':
            form = CartForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data['quantity']
                if product.status == 'None':
                    if check == 'yes':
                        shop = Cart.objects.get(user_id=request.user.id,product_id=id)
                        shop.quantity += data
                        shop.save()
                    else:
                        Cart.objects.create(user_id=request.user.id,product_id=id,quantity=data)
            return redirect(url)





def remove_cart(request,id):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=id).delete()
    return redirect(url)
