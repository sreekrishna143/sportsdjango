from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

class Player(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_images/')
    description = models.TextField()
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ['country', 'name']

    def __str__(self):
        return self.name

class Feedback(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.username