from django.shortcuts import render
from django.views import generic
from .models import Profile
from allauth.account.views import SignupView
from .forms import CustomSignupForm
from django.shortcuts import redirect, render

class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    success_url = '/accounts/login'

    def form_valid(self, form):
        response = super().form_valid(form)

        return response

class ProfileList(generic.ListView):
    model = Profile
    template_name = 'index.html'
    context_object_name = 'profiles'