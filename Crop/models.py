from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(max_length=100, unique=True)
    Age = models.IntegerField()
    Phone_Number = models.CharField(max_length=15, unique=True)
    Password = models.CharField(max_length=100)

class Crop(models.Model):
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temprature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()