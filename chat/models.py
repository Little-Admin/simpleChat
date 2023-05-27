from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Friends(models.Model):
    user = models.ForeignKey(User, related_name='User_friends_set', null=True, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.user.username} friends"

class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)