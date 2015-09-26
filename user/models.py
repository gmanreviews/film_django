from django.db import models

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def create_location(self):
        location = self.create()
        return location

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    location = models.ForeignKey(Location)

    def create_person(self):
        person = self.create()
        return person

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    person = models.ForeignKey(Person)

    def create_user(self):
        user = self.create_user()
        return user

    def create_user(self, username, password, person):
        user = self.create(username=username,password=password,person=person)
        return user

    def autheticate_user(username, password):
        result = 0
        try:
            user = User.objects.get(username=username);
            result = password == user.password
        except:
            result = 0
        return result