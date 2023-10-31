from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name", required=True)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True)
    username = forms.CharField(max_length=20, label="Username", required=True)
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Enter your first name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Enter your last name'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Enter a username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Enter your email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter a password'})
