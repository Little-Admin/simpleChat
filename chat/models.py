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

class Message(models.Model):
    friends_room = models.CharField(max_length=10)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)