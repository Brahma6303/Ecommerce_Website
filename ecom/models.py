from django.db import models

# Create your models here.

class User_Register(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.username