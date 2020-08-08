from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    
    
class extenduser(models.Model):
    phone_num=models.CharField(max_length=15)
    age=models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    
    
class memory(models.Model):
    content=models.TextField()
    date=models.DateField(("Date"),default=datetime.date.today)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    