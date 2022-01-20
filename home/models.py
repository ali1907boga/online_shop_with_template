from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
from django import forms

class Category(models.Model):

    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category/',null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    VARIENT_CHOICES = (

        ('None','none'),
        ('Color','color'),
        ('Size','size')


    )

    category = models.ForeignKey(Category,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    favourite = models.ManyToManyField(User,related_name = 'fa_pro',blank=True,null=True)
    total_price = models.PositiveIntegerField()
    information = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/')
    status = models.CharField(max_length=100,choices=VARIENT_CHOICES,null=True,blank=True)

    def average(self):
        data = Comment.objects.filter(is_reply=False,product=self).aggregate(avg=Avg('rate'))
        star = 0
        if data['avg'] is not None:
            star = round(data['avg'],2)
        return star




    def __str__(self):
        return self.name


    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = self.discount * self.unit_price / 100
            return int(self.unit_price - total)
        return self.total_price

class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Variant(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    varient_size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True,blank=True)
    varient_color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    product_varient = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='pro_var')
    amount = models.PositiveIntegerField(default=0)
    unit_price = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property

    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = int(self.unit_price * self.discount) / 100
            return self.unit_price - total
        return self.total_price


class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.PositiveIntegerField(default=1)
    create = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    reply = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='com_reply')
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user','email','comment','rate']


class Image_pro(models.Model):

    product_img = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    image_pro = models.ImageField(upload_to='image_pro/',null=True,blank=True)
