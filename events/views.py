from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Invitation
from .forms import EventForm, InvitationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F

@login_required
def event_list(request):
    public_events = Event.objects.filter(is_private=False).order_by('date')
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
    return render(request, 'create_event.html', {'form': form})


def delete_event(request, event_id):
    # Check if the user is logged in
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page

    # Get the event by ID
    event = get_object_or_404(Event, id=event_id)

    # Check if the user is the creator of the event
    if request.user == event.creator:
        # Delete the event
        event.delete()

    return redirect('event_list')  # Redirect to the event list page
    
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