from django.db import models

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    location = models.ForeignKey(Location)

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    person = models.ForeignKey(Person)


