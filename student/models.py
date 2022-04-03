from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class student(models.Model):
      firstname= models.CharField(max_length=200)
      lastname= models.CharField(max_length=200)
      id=models.IntegerField(primary_key=True)
      email=models.EmailField()
      department= models.CharField(max_length=200)
      gender= models.CharField(max_length=200)
      phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
      phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
      