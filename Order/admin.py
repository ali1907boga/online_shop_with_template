from django.contrib import admin
from .models import *

class ItemOrderInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['user','product','quantity']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','email','f_name','l_name','address','create','paid','code']
    inlines = [ItemOrderInline,]


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','start','end','discount','active']


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Coupon)
