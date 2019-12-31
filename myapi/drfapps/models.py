from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import date,datetime

from django.db import models


from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
# accounts.models.py



class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "student"


class MyclubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Subscriber(MyclubUser):
    date_joined = models.DateTimeField()


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip/Post Code', max_length=12)
    phone = models.CharField('Contact Phone', max_length=20, blank=True)
    web = models.URLField('Web Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name

class EventManager(models.Manager):
      def event_type_count(self, event_type):
          return self.filter(name__icontains=event_type).count()



class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(MyclubUser)
    description = models.TextField(blank=True)
    events = EventManager()

    def event_timing(self, date):
        if self.event_date > date:
            print("aa")
            return "Event is after this date"
        elif self.event_date == date:
            print("b")
            return "Event is on the same day"
        else:
            print("c")
            return "Event is befor this date"



    @property
    def name_slug(self):
        return self.name.lower().replace(' ', '-')


    def __str__(self):
        return self.name