
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.

#____ create HomePage Object ____#
class HomePage(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)  # name to identify homepage object
    heading = models.CharField(max_length=100, unique=True)                 # website heading
    sub_title = models.CharField(max_length=100, unique=True)
    stamp = models.TextField(max_length=80)                         # website <about> description
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=200)

    def __repr__(self):
        return f"{self.name}"


#____ create SlideImages Object ____#
class Poster(models.Model):
    name = models.CharField(max_length=100)
    imagefile = models.ImageField(upload_to='static/media/flyers/', blank=True, null=True, verbose_name="")
    alternate_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


#____ create SocialMedia Object ____#
class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    profile_link = models.CharField(max_length=500)
    icon = models.ImageField(upload_to='static/media/icons/', blank=True, null=True, verbose_name="")

    def __str__(self):
        return f"{self.name}"
