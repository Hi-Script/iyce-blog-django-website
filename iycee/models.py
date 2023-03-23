from ctypes import resize
from distutils.command.upload import upload
import email
from email.policy import default
from pickle import TRUE
from statistics import mode
from turtle import title, update
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Features(models.Model):
    
    title = models.CharField(max_length= 150, null=True, blank=TRUE)
    description = models.TextField(null=TRUE, blank=TRUE)
    body = models.TextField(null=TRUE, blank=TRUE)
    post_pic = models.ImageField(null=TRUE, blank=TRUE, upload_to='feature/')
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=TRUE)
    created= models.DateTimeField(auto_now_add=TRUE,null=TRUE)
    updated= models.DateTimeField(auto_now=TRUE, null=TRUE)

    class Meta:
        ordering =['-created']

    def __str__(self):
        return self.title  



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    fullname = models.CharField(max_length = 150, null=TRUE, blank=TRUE)
    email = models.EmailField(null=TRUE, blank=TRUE)
    phone = models.CharField(max_length = 100, null=TRUE, blank=TRUE)
    image = models.ImageField(default= 'default.png', upload_to ='profile_pic', null=TRUE, blank=TRUE)

    def __str__(self):
        return f"{self.user.username} Profile"




class Comment(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    comment = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=TRUE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment


class Post(models.Model):
    title= models.CharField(max_length=100, null=TRUE)
    description = models.TextField(null=TRUE, blank=TRUE)
    body = models.TextField(null=TRUE)
    post_pic = models.ImageField(null=TRUE, blank=TRUE, upload_to='images/')
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=TRUE)
    created= models.DateTimeField(auto_now_add=TRUE,null=TRUE)
    updated= models.DateTimeField(auto_now=TRUE, null=TRUE)

    class Meta:
        ordering =['-created']

    def __str__(self):
        return self.title  


