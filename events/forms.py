from django import forms
from .models import Event, Invitation

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'is_private']


# Needs to added with choices of friends or something AND remember to add Invitation to import next to Event
class InvitationForm(forms.Form):
    invited_email = forms.EmailField(label='Email')
