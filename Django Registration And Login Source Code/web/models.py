from django.db import models

# Create your models here.

class Member(models.Model):
    Name=models.CharField(max_length=30,null=True)
    Email=models.CharField(max_length=30,null=True)
    Username=models.CharField(max_length=30,null=True)
    Password=models.CharField(max_length=30,null=True)
    Address=models.CharField(max_length=300,null=True)


    def __str__(self):
        return self.Name