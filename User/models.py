from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.CharField(max_length=10, primary_key=True, unique=True)
    username = models.CharField(max_length=100, unique=True, null=False)
    email = models.CharField(unique=True)
    password_hash = models.CharField(max_length=255, null=False)
    role_choices = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    role = models.ChoicesField(choices=role_choices, default='client')
    
    
    class Meta:
        db_table = 'User'