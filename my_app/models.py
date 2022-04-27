from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class work_type(models.Model):
     work_type = models.CharField(max_length=100)

class category(models.Model):
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=100)



class user_register(models.Model):
    fullname =  models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password  = models.CharField(max_length=100)
    username  = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.SET_NULL,related_name='dep', null=True, blank=True, default='')
    regdate=models.DateField(default='')
    status = models.CharField(max_length=20,default='0')
    photo = models.FileField(upload_to='images/', null=True, blank=True)

class work_details(models.Model):
    work_type = models.ForeignKey(work_type, on_delete=models.SET_NULL, related_name='desgn',null=True,blank=True, default='')
    work_name = models.CharField(max_length=200)
    contact_no=models.CharField(max_length=200,default='')
    work_details = models.CharField(max_length=300)
    category_id = models.ForeignKey(category, on_delete=models.SET_NULL,related_name='worker_dep', null=True, blank=True, default='')
    work_status = models.CharField(max_length=20,default='0')
    worker_id= models.ForeignKey(user_register, on_delete=models.SET_NULL,related_name='worker_id', null=True, blank=True, default='')

class feedback(models.Model):
    work_name = models.CharField(max_length=200)
    work_type = models.ForeignKey(work_type, on_delete=models.SET_NULL, related_name='worktyp',null=True,blank=True, default='')
    work_name = models.CharField(max_length=200)
    post_date=models.CharField(max_length=200,default='')
    feedback_replay = models.CharField(max_length=300)
    category_id = models.ForeignKey(category, on_delete=models.SET_NULL,related_name='worker_deptment', null=True, blank=True, default='')
    replay_status = models.CharField(max_length=20,default='0')