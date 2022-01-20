from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from home.models import *
from Order.models import *

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['username'],email=data['email'],password=data['password_2'])
            user.save()
            return redirect('home:home')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request,username=User.objects.get(email=data['user']),password=data['password'])
            except:
                user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'به سایت خوش آمدید','primary')
                return redirect('home:home')
            else:
                messages.error(request,'رمز یا نام کاربری اشتباه است','danger')
    else:
        form = UserLoginForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,'logout','primary')
    return redirect('home:home')

def user_profile(request):

    profile = Profile.objects.get(user_id=request.user.id)
    return render(request,'profile.html',{'profile':profile})


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdate(request.POST, instance=request.user)
        profile_form = ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)

        if profile_form and user_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        profile_form = ProfileUpdate(instance=request.user.profile)
        user_form = UserUpdate(instance=request.user)
    return render(request,'update.html',{'user_form':user_form,'profile_form':profile_form})

def user_change(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'change password successfully','success')
            return redirect('accounts:profile')
        else:
            messages.success(request,'wrong password','danger')
            return redirect('accounts:change')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'change.html',{'form':form})

def favorite(request):
    product = request.user.fa_pro.all()
    num = request.user.fa_pro.count()
    return render(request,'favorite.html',{'product':product,'num':num})

def num_fav(request):
    num1 = request.user.fa_pro.count()
    return render(request,'template/base.html',{'num1':num1})

def history(request):
    data = OrderItem.objects.filter(user_id=request.user.id)
    return render(request,'hsitory.html',{'data':data})
