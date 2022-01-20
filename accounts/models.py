from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField(null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='profile/',null=True,blank=True)

    def __str__(self):
        return self.user.username

def user_profile(sender,**kwargs):
    if kwargs['created']:
        profile = Profile(user=kwargs['instance'])
        profile.save()


post_save.connect(user_profile,User)




