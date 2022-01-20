from django.db import models
from django.contrib.auth.models import User
from home.models import *
from django import forms

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)
    discount = models.IntegerField(null=True,blank=True)
    f_name = models.TextField()
    l_name = models.TextField()
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=8,null=True,blank=True)

    def __str__(self):
        return self.user.username

    def get_price(self):
        total = sum( i.price() for i in self.order_item.all())
        if self.discount:
            discount_price = (self.discount / 100 )* total
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_item')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()



    def __str__(self):
        return self.user.username

    def price(self):
        if self.product.status == 'None':
            return self.product.total_price * self.quantity


class Coupon(models.Model):
    code = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    start = models.DateTimeField()
    end = models.DateTimeField()
    discount = models.IntegerField()





class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user','f_name','l_name','email','address']
