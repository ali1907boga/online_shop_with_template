from django.db import models
from home.models import *
from django import forms

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    code = models.CharField(max_length=8)

    def __str__(self):
        return self.product.name

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']