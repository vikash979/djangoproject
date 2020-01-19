from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.contrib.auth.models import CustomUser

from django.db.models.signals import post_save
from django.dispatch import receiver



class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'teacher'),
        (3, 'secretary'),
        (4, 'supervisor'),
        (5, 'student'),
    )
    admin = models.IntegerField(choices=USER_TYPE_CHOICES, default='1')
    # add additional fields in here

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        print("hello")
        return self.user.username

@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    print("bye")
    if created:
        print("ok")
        Profile.objects.create(user=instance)
    instance.profile.save()

class blog(models.Model):
   
    title = models.CharField(max_length=200)
    created_on = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200)
    content = models.TextField()


    # def __str__(self):
    #     print("fdfdfdf")
    #     return self.title
