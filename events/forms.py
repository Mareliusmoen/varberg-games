from django import forms
from .models import Event, Invitation

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'is_private']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'placeholder': 'The title of your event'})
        self.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'Describe the game/format, power-level, bring drinks, or whatever describes the event', 'class': 'custom-textarea'})
        self.fields['date'].widget = forms.DateTimeInput(attrs={'placeholder': 'Select date and time', 'class': 'datetimepicker-input', 'id': 'datetimepicker'})


# Needs to added with choices of friends or something AND remember to add Invitation to import next to Event
class InvitationForm(forms.Form):
    invited_email = forms.EmailField(label='Email')
