from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class timeZone(models.Model):
    tzname = models.CharField(max_length=30)

class userTimeZone(models.Model):
    user = models.ForeignKey(User, related_name='timeZone', on_delete=models.CASCADE)
    timeZone = models.CharField(max_length=30, default='UTC')