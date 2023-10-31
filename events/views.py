from django.shortcuts import render, redirect
from .models import Event, Invitation
from .forms import EventForm, InvitationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def event_list(request):
    public_events = Event.objects.filter(is_private=False)
    return render(request, 'events.html', {'public_events': public_events})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            messages.success(request, 'Event created successfully.')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event/create_event.html', {'form': form})

# Need to work out how to invite with the username instead


# @login_required
# def invite_to_event(request, event_id):
#     event = Event.objects.get(id=event_id)
    
#     if request.method == 'POST':
#         form = InvitationForm(request.POST)
#         if form.is_valid():
#             invited_email = form.cleaned_data['invited_email']
#             # Check if the user with the provided email exists
#             try:
#                 invited_user = User.objects.get(email=invited_email)
#                 invitation_code = "generate_unique_code_here"
#                 invitation = Invitation(event=event, invited_user=invited_user, invitation_code=invitation_code)
#                 invitation.save()
#                 messages.success(request, 'Invitation sent successfully.')
#                 return redirect('event_list')
#             except User.DoesNotExist:
#                 messages.error(request, 'User with the provided email does not exist.')
#     else:
#         form = InvitationForm()
#     return render(request, 'event/invite_to_event.html', {'form': form, 'event': event})