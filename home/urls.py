from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    path('',views.home,name='home'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('all_product/',views.all_product,name='all_product'),
    path('products/<int:id>/',views.all_product,name='product'),
    path('category/<int:id>/',views.home,name='category'),
    path('favorite/<int:id>/',views.favourite,name='fav_pro'),
    path('comment/<int:id>/',views.comment,name='comment'),
    path('search/',views.search,name='search'),



]