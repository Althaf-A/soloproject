from django.contrib.auth.models import User
from django.db import models

# Create your models here.


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
    regdate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=20,default='0')
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    experience = models.CharField(max_length=20,default='0')
    work_name = models.CharField(max_length=200)
   

    

class feedback(models.Model):
    user_id= models.ForeignKey(user_register, on_delete=models.SET_NULL,related_name='userid', null=True, blank=True, default='')
    worker_id= models.ForeignKey(user_register, on_delete=models.SET_NULL,related_name='worker1', null=True, blank=True, default='')
    work =  models.CharField(max_length=300,default='')
    from_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    to_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    post_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    replay_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    feedback = models.CharField(max_length=300)
    feedback_replay = models.CharField(max_length=300)
    replay_status = models.CharField(max_length=20,default='0')
    work_status = models.CharField(max_length=20,default='0')

class enquiry(models.Model):
    user_id= models.ForeignKey(user_register, on_delete=models.SET_NULL,related_name='useride', null=True, blank=True, default='')
    worker_id= models.ForeignKey(user_register, on_delete=models.SET_NULL,related_name='worker1e', null=True, blank=True, default='')
    enquiry = models.CharField(max_length=300)
    enquiry_replay = models.CharField(max_length=300)
    status = models.CharField(max_length=20,default='0')

