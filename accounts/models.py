from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(unique=True,max_length=264,verbose_name='Email Address')
    country=models.CharField(max_length=264,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    gender=models.CharField(choices=(('Male','male'),('Female','female'),('Prefer not to say','no_preferance')),max_length=264)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username']

    def __str__(self):
        return self.email
