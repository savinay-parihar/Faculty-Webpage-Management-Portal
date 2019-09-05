# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required
from django.views  import generic
import datetime

# Create your models here

class signup(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    album_logo = models.FileField()


    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User)
    webmail = models.CharField(max_length=200,default='')
    Faculty_name=models.CharField(max_length=300,default='')
    Department = models.CharField(max_length=300,default='')
    Academic_position = models.CharField(max_length=300,default='')
    Phone = models.IntegerField(default=0)
    RoomNo = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_image/',blank=True,default='media/profile_image/400x400.png')
    About = models.CharField(max_length=2000)
    linkedin = models.CharField(max_length=300,default='')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



class Qualification(models.Model):
    user = models.OneToOneField(User)
    Undergraduate = models.CharField(max_length=300,default='')
    Postgraduate = models.CharField(max_length=300,default='')
    Phd = models.CharField(max_length=300,default='')
    Undergraduate_college=models.CharField(max_length=300,default='')
    Postgraduate_college = models.CharField(max_length=300, default='')
    Phd_college=models.CharField(max_length=300,default='')
    Undergraduate_year = models.IntegerField(default=0)
    Postgraduate_year = models.IntegerField(default=0)
    Phd_year=models.IntegerField(default=0)


    def __str__(self):
        return self.user.username


def create_qualification(sender, **kwargs):
    if kwargs['created']:
        user_qualification = Qualification.objects.create(user=kwargs['instance'])

post_save.connect(create_qualification, sender=User)

class Teaching(models.Model):
    user = models.ForeignKey(User)
    status = models.CharField(max_length=100,default='')
    year = models.CharField(max_length=200,default='')
    semester = models.CharField(max_length=200,default='')
    Course_name = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.user.username




class Project(models.Model):
    user = models.ForeignKey(User)
    Title = models.CharField(max_length=500,default='')
    Sponser = models.CharField(max_length=300,default='')
    start_year = models.CharField(max_length=200,default='')
    end_year = models.CharField(max_length=200,default='')
    Role = models.CharField(max_length=500,default='')
    Description=models.CharField(max_length=2000,default='')

    def __str__(self):
        return self.user.username



class Publication(models.Model):
    user = models.ForeignKey(User)
    Type = models.CharField(max_length=300,default='')
    Title = models.CharField(max_length=300,default='')
    Description = models.CharField(max_length=1000,default='')


    def __str__(self):
        return self.user.username





class Experience(models.Model):
    user = models.ForeignKey(User)
    start_year = models.CharField(max_length=100,default='')
    end_year = models.CharField(max_length=100,default='')
    About = models.CharField(max_length=1000,default='')
    Responsibility = models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.user.username


