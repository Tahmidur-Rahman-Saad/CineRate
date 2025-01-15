from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Director(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers', null = True)
    date_of_birth = models.DateField(null=True, blank=True)
    Nationality = models.CharField(max_length=20)
    image = models.ImageField(upload_to='director_images/', null=True, blank=True)


    


class Cast(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers', null = True)
    date_of_birth = models.DateField(null=True, blank=True)
    Nationality = models.CharField(max_length=20)
    image = models.ImageField(upload_to='director_images/', null=True, blank=True)
    gender = models.BooleanField(default=None)



class Authorizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers', null = True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    nid = models.CharField(max_length=15,null = True,blank=True)
    image = models.ImageField(upload_to='authorizer_images/', null=True, blank=True)




class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers', null = True)
    image = models.ImageField(upload_to='authorizer_images/', null=True, blank=True)
    age = models.IntegerField(default=18)
    gender = models.BooleanField(default=None)