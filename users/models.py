from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Person(AbstractUser):
    CIN = models.CharField('CIN', max_length=8, primary_key=True)
    username = models.CharField('username', max_length=255, unique=True)
    email = models.EmailField('email', max_length=255)
    
    USERNAME_FIELD = 'username'
    
    class Meta:
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"
    