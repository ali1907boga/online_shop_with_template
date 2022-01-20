from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [

    path('order_detail/<int:id>/',views.order_detail,name='order_detail'),
    path('order_create/',views.order_create,name='order_create'),
    path('coupon/<int:order_id>/',views.coupon,name='coupon')



]