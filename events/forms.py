from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'is_private']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'placeholder': 'The title of your event'})
        self.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'Describe the game/format, power-level, bring drinks, or whatever describes the event', 'class': 'custom-textarea'})
        self.fields['date'].widget = forms.DateTimeInput(attrs={'placeholder': 'Select date and time', 'class': 'datetimepicker-input', 'id': 'datetimepicker'})


class AccessCodeForm(forms.Form):
    access_code = forms.CharField(max_length=10, label="Enter Access Code")


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your comment here...', 'class': 'custom-textarea'}))