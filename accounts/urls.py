from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='login'),
    path('user_logout/',views.user_logout,name='logout'),
    path('user_profile/',views.user_profile,name='profile'),
    path('user_update/',views.user_update,name='update'),
    path('user_change/',views.user_change,name='change'),
    path('favorite/',views.favorite,name='favorite'),
    path('num_fav/',views.num_fav,name='num_fav'),
    path('history/',views.history,name='history'),



]