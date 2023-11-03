from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import secrets
import string


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    is_private = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='events_attending')
    access_code = models.CharField(max_length=10, null=True, blank=True)
    comments = models.ManyToManyField('Comment', blank=True, related_name='event_comments')

    def has_already_passed(self):
        return self.date < timezone.now()

def generate_access_code():
    return ''.join(secrets.choice(string.digits) for _ in range(10))

class EventParticipant(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}: {self.text[:50]}"  # Display part of the comment text
