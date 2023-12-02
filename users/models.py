from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.
def email_Validator (value):
    if str(value).endswith("@esprit.tn") == False:
        raise ValidationError("Your email must be @esprit.tn")
    return value

def cin_length (value):
    if len(value) != 8:
        raise ValidationError("Your CIN must have 8 characters!")
    return value
class Person(AbstractUser):
    CIN = models.CharField('CIN', max_length=8, primary_key=True, validators = [
        MinLengthValidator(8), MaxLengthValidator(8), cin_length]
    )
    
    username = models.CharField('username', max_length=255, unique=True)
    email = models.EmailField('email', max_length=255)
    
    USERNAME_FIELD = 'username'
    
    class Meta:
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"
    