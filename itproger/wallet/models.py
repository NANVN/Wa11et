from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, null=True)



