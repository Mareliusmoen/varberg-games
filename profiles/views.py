from django.shortcuts import render
from django.views import generic
from .models import Profile


class ProfileList(generic.ListView):
    model = Profile
    template_name = 'index.html'
    context_object_name = 'profiles'