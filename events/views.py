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
    """
    Renders a list of events.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered events template.
    """
    if request.method == "POST":
        # Handle access code submission
        form = AccessCodeForm(request.POST)
        if form.is_valid():
            access_code = form.cleaned_data["access_code"]
            # Iterate over all events to find the matching access code
            for event in Event.objects.filter(is_private=True):
                if event.access_code == access_code:
                    # Add the user as a participant to the event
                    event.participants.add(request.user)
                    messages.success(
                        request,
                        "You have successfully joined the private event.")
                    return redirect('joined_events')

            # If no event matched the access code, display an error message
            messages.error(request, "Invalid access code. Please try again.")

    public_events = Event.objects.filter(is_private=False).order_by('date')
    return render(
        request,
        'events.html',
        {'public_events': public_events, 'form': AccessCodeForm()}
    )


@login_required
def create_event(request):
    """
    Creates an event based on the data submitted through a POST request. 

    Parameters:
        - request: The HTTP request object containing the form data.

    Returns:
        - If the event creation is successful, redirects the user to the event list page.
        - If the request method is not POST, renders the create event form.
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            event.participants.add(request.user)
            if event.is_private:
                event.access_code = generate_access_code()
                event.save()
            messages.success(request, 'Event created successfully.')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

# Function to generate a random access code


def generate_access_code():
    """
    Generates an access code consisting of 10 random characters, including both letters (uppercase and lowercase) and digits.

    Returns:
        str: The randomly generated access code.
    """
    length = 10
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@login_required
def edit_event(request, event_id):
    """
    Edits an event based on the given event ID.

    Parameters:
        request (HttpRequest): The HTTP request object.
        event_id (int): The ID of the event to be edited.

    Returns:
        HttpResponse: The response containing the edited event form and event data if the user has permission to edit the event. Otherwise, redirects to the joined events page.
    """
    # Get the event by ID
    event = get_object_or_404(Event, id=event_id)

    # Checks if the logged in user is the creator of the event
    if request.user == event.creator:
        if request.method == 'POST':
            # form is filled in with the existing data
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                # Save the updated event
                form.save()
                messages.success(
                    request, "You have successfully edited the event.")
                return redirect('joined_events')
        else:
            # Display the form with existing data
            form = EventForm(instance=event)

        # Pass both the form and the event to the template
        return render(
            request, 'edit_event.html', {'form': form, 'event': event})
    else:
        messages.error(
            request, "You do not have permission to edit this event.")
        return redirect('joined_events')


@login_required
def delete_event(request, event_id):
    """
    Deletes an event.

    Parameters:
        request (HttpRequest): The HTTP request object.
        event_id (int): The ID of the event to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the 'joined_events' page.

    Raises:
        None.
    """
    # Check if the user is logged in
    if not request.user.is_authenticated:
        return redirect('login')

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
    """
    Adds the logged-in user to the participants of the specified event.

    Parameters:
        request (HttpRequest): The HTTP request object.
        event_id (int): The ID of the event to join.

    Returns:
        HttpResponseRedirect: A redirect to the event list page.

    Raises:
        Event.DoesNotExist: If the specified event does not exist.
    """
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
    """
    Renders a template with a list of events in which the logged-in user is a participant.

    Parameters:
        - request: The HTTP request object.

    Returns:
        - If the user is authenticated, the function renders a template 'joined_events.html' with the list of events in which the user is a participant.
        - If the user is not authenticated, the function renders a template 'joined_events.html' without any events.
    """
    if request.user.is_authenticated:
        # Filter events where the logged-in user is a participant
        user_participating_events = Event.objects.filter(
            participants=request.user)
        context = {'user_participating_events': user_participating_events}
        return render(request, 'joined_events.html', context)
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'joined_events.html')


@login_required
def enter_access_code(request):
    """
    Validates and processes the access code entered by the user.

    Parameters:
        - request (HttpRequest): The HTTP request object containing
        metadata about the request.

    Returns:
        - HttpResponseRedirect: A redirect response to the 'joined_events'
        page if the access code is valid.
        - HttpResponse: A rendered HTML response displaying the 'events.html'
        template with the access code form.

    Raises:
        - None

    Description:
        - This function is decorated with the 'login_required' decorator,
        which ensures that the user must be authenticated in order to access
        this view.
        - The function first checks if the request method is 'POST'. If it is,
        it initializes an 'AccessCodeForm' object with the
        POST data and checks if the form is valid.
        - If the form is valid, it retrieves the access code entered
        by the user.
        - It then iterates over all events that have the 'is_private' flag set
        to 'True' and compares their access codes with
        the one entered by the user.
        - If a matching access code is found, the user is added as a
        participant to the event and a success message is displayed.
        The function then redirects the user to the 'joined_events' page.
        - If no event matches the access code, an error message is displayed.
        - If the request method is not 'POST', the function initializes an
        empty 'AccessCodeForm'.
        - Finally, the function renders the 'events.html' template with the
        'form' variable as context.

    Note:
        - This function assumes that the 'AccessCodeForm' and 'Event' models
        are properly defined and imported.
        - The 'messages' object is assumed to be a Django Messages Framework
        object for displaying success and error messages.
        - The 'reverse' function is assumed to be a Django utility function for
        generating URLs based on URL patterns.
    """
    if request.method == "POST":
        form = AccessCodeForm(request.POST)
        if form.is_valid():
            access_code = form.cleaned_data["access_code"]
        # Iterate over all events to find the one with the matching access code
            for event in Event.objects.filter(is_private=True):
                if event.access_code == access_code:
                    # Add the user as a participant to the event
                    event.participants.add(request.user)
                    messages.success(
                        request,
                        "You have successfully joined the private event."
                    )
                    return HttpResponseRedirect(reverse('joined_events'))
            # If no event matched the access code, display an error message
            messages.error(request, "Invalid access code. Please try again.")
    else:
        form = AccessCodeForm()

    return render(request, "events.html", {"form": form})


@login_required
def event_detail(request, event_id):
    """
    Renders the detail view for a specific event.

    Parameters:
        request (HttpRequest): The HTTP request object.
        event_id (int): The ID of the event to display.

    Returns:
        HttpResponse: The rendered HTML response for the event detail page.
    """
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
            messages.success(
                request, "You have successfully commented on this event.")
            return redirect('event_detail', event_id=event_id)

    context = {'event': event, 'comments': comments,
               'comment_form': comment_form}
    return render(request, 'event_detail.html', context)


@login_required
def add_comment(request, event_id):
    """
    Adds a comment to an event.

    Parameters:
        - request: The HTTP request object.
        - event_id: The ID of the event to add the comment to.

    Returns:
        - HttpResponse: The HTTP response object.
    """
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user = request.user
            comment = Comment(event=event, user=user, text=text)
            comment.save()
            messages.success(
                request, "You have successfully commented on this event.")
            return redirect('event_detail', event_id=event_id)
    else:
        form = CommentForm()

    return render(
        request,
        'event_detail.html',
        {
            'event': event,
            'comment_form': form
        }
    )


@login_required
def delete_comment(request, comment_id):
    """
    Deletes a comment.

    Args:
        request (HttpRequest): The HTTP request object.
        comment_id (int): The ID of the comment to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the event detail page.
    """
    # Check if the user is logged in
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page

    # Get the comment by ID
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is the author of the comment
    if request.user == comment.user:
        # Delete the comment
        comment.delete()
        messages.success(request, "You have successfully deleted the comment.")
    else:
        messages.error(
            request, "You are not authorized to delete this comment.")

    return redirect('event_detail', event_id=comment.event.id)
