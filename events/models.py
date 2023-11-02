from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    is_private = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='events_attending')

    def has_already_passed(self):
        return self.date < timezone.now()

class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE)
    invitation_code = models.CharField(max_length=10, unique=True)

class EventParticipant(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)