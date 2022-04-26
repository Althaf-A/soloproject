from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class designation(models.Model):
     designation = models.CharField(max_length=100)

class login(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.SET_NULL, related_name='desgn',null=True,blank=True, default='')
    fullname = models.CharField(max_length=200)
    email=models.EmailField(max_length=200,default='')
    contact_no=models.CharField(max_length=200,default='')
    password = models.CharField(max_length=100)
    image = models.FileField(upload_to= 'images/')

class department(models.Model):
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=100)

class candidates (models.Model):
    fullname =  models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password  = models.CharField(max_length=100)
    username  = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    deptmnt = models.ForeignKey(department, on_delete=models.SET_NULL,related_name='dep', null=True, blank=True, default='')
    regdate=models.DateField(default='')
    status = models.CharField(max_length=20,default='0')
