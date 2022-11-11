from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Complaint(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    residence = models.CharField(max_length=50)
    problem = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default= '')
   
    
    def __str__(self):
        return 'Name: {},Id: {}'.format(self.first_name,self.id)
