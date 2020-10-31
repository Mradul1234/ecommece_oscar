from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reward_points(models.Model):
    user_of_points = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    points = models.IntegerField()
