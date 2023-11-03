from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, EventParticipant, Comment
from .models import generate_access_code
from .forms import EventForm, AccessCodeForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from django.urls import reverse
import string
import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

@login_required
def event_list(request):
    if request.method == "POST":
        # Handle access code submission
        form = AccessCodeForm(request.POST)
        if form.is_valid():
            access_code = form.cleaned_data["access_code"]
            # Iterate over all events to find the one with the matching access code
            for event in Event.objects.filter(is_private=True):
                if event.access_code == access_code:
                    # Add the user as a participant to the event
                    event.participants.add(request.user)
                    messages.success(request, "You have successfully joined the private event.")
                    return redirect('joined_events')

            # If no event matched the access code, display an error message
            messages.error(request, "Invalid access code. Please try again.")

    public_events = Event.objects.filter(is_private=False).order_by('date')
    return render(request, 'events.html', {'public_events': public_events, 'form': AccessCodeForm()})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            event.participants.add(request.user)
            if event.is_private:
                event.access_code = generate_access_code()  # Generate and assign access code
                event.save()
            messages.success(request, 'Event created successfully.')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

# Function to generate a random access code
def generate_access_code():
    length = 10
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@login_required
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
    messages.success(request, "You have successfully deleted the event.")
    return redirect('joined_events')  # Redirect to the joined events page

@login_required
def join_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user not in event.participants.all():
        event.participants.add(request.user)
        EventParticipant.objects.create(event=event, user=request.user)

        if request.user not in event.participants.all():
            event.participants.add(request.user)
            event.save()

        # Add a success message
        messages.success(request, "You have successfully joined the event!")

    return redirect('event_list')

def joined_events(request):
    if request.user.is_authenticated:
        # Filter events where the logged-in user is a participant
        user_participating_events = Event.objects.filter(participants=request.user)
        context = {'user_participating_events': user_participating_events}
        return render(request, 'joined_events.html', context)
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'joined_events.html')


@login_required
def enter_access_code(request):
    if request.method == "POST":
        form = AccessCodeForm(request.POST)
        if form.is_valid():
            access_code = form.cleaned_data["access_code"]
            # Iterate over all events to find the one with the matching access code
            for event in Event.objects.filter(is_private=True):
                if event.access_code == access_code:
                    # Add the user as a participant to the event
                    event.participants.add(request.user)
                    messages.success(request, "You have successfully joined the private event.")
                    return HttpResponseRedirect(reverse('joined_events'))
            # If no event matched the access code, display an error message
            messages.error(request, "Invalid access code. Please try again.")
    else:
        form = AccessCodeForm()

    return render(request, "events.html", {"form": form})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    comments = Comment.objects.filter(event=event)

    # Create an instance of the CommentForm
    comment_form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user = request.user
            comment = Comment(event=event, user=user, text=text)
            comment.save()
            messages.success(request, "You have successfully commented on this event.")
            return redirect('event_detail', event_id=event_id)
    
    context = {'event': event, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'event_detail.html', context)

@login_required
def add_comment(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user = request.user
            comment = Comment(event=event, user=user, text=text)
            comment.save()
            messages.success(request, "You have successfully commented on this event.")
            return redirect('event_detail', event_id=event_id)
    else:
        form = CommentForm()

    return render(request, 'event_detail.html', {'event': event, 'comment_form': form})
