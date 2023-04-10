from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    earn = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    spend = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    start_time = models.DateTimeField(null=True)
    id = models.ForeignKey(Profile, on_delete=models.CASCADE, primary_key=True)

