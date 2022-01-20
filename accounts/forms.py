from django import forms
from django.contrib.auth.models import User
from .models import Profile

error = {

    'required':'this field is required'

}

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=100,error_messages=error,widget=forms.TextInput(attrs={'placeholder':'username'}))
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'placeholder':'email'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password_2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'re_pass'}))


    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exist')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exist')
        return email

    def clean_password_2(self):
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_2']
        if password_1 != password_2:
            raise forms.ValidationError('not match password')
        elif len(password_1) < 8:
            raise forms.ValidationError('less than 8 character must more than 8 character password')
        return password_2

class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placehoder':'usernaem or email'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'password'}))


class UserUpdate(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone','address','image']