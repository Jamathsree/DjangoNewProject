from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models



class Login(AbstractUser):
    is_Customer=models.BooleanField(default=False)
    is_Worker = models.BooleanField(default=False)


class Services(models.Model):
    name = models.CharField(max_length=30,unique=True)


# Worker model
class Worker(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True,null=True)
    address = models.TextField()
    phone_number = models.IntegerField()
    location = models.TextField()
    image = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.name

class Worker_schedule(models.Model):
    user=models.ForeignKey(Worker,on_delete=models.CASCADE)
    start_time=models.TimeField('start_time')
    end_time=models.TimeField('end_time')
    date=models.DateField()

# Customer models
class Customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=30,unique=True,null=True)
    address = models.TextField()
    phone_number = models.IntegerField()
    location = models.TextField()
    # image = models.ImageField(upload_to='images/', null=True)
    def __str__(self):
        return self.name


class Appoinment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    Worker_schedule = models.ForeignKey(Worker_schedule,on_delete=models.CASCADE,null=True,blank=True)
    status = models.IntegerField(default=0)

class Complaint(models.Model):
   user = models.ForeignKey(Login, on_delete= models.CASCADE)
   date = models.DateField(default=datetime.now)
   content = models.CharField(max_length=200, null=True)
   reply = models.CharField(max_length=200,null=True,blank=True)

