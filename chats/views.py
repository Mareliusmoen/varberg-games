from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Chat, Message
from django.db.models import Q

def chats_view(request):
    # Retrieve a list of chat conversations that the logged-in user is a part of
    user = request.user
    chat_conversations = Chat.objects.filter(users=user)

    context = {
        'chat_conversations': chat_conversations,
    }

    return render(request, 'chats.html', context)
def user_search(request):
    search_query = request.GET.get("search_query", "")
    users = User.objects.filter(
        Q(username__icontains=search_query)
        | Q(first_name__icontains=search_query)
        | Q(last_name__icontains=search_query)
    ).values("id", "username", "first_name", "last_name")

    return JsonResponse({"users": list(users)})


def fetch_chat_history(request):
    user_id = request.GET.get("user_id")
    # Implement a query to retrieve chat history with the selected user
    messages = Message.objects.filter(
    Q(sender=request.user, receiver_id=user_id) | Q(sender_id=user_id, receiver=request.user)).order_by('timestamp')

    chat_history = []
    for message in messages:
        chat_history.append({
            'content': message.content,
            'sender_id': message.sender_id,
        })

    return JsonResponse({'messages': chat_history})


def send_message(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        message_content = request.POST.get("message")

        # Retrieve the user corresponding to user_id
        receiver_user = User.objects.get(id=user_id)

        # Create a Message object and save it to the database
        message = Message(
            sender=request.user,
            receiver=receiver_user,
            content=message_content
        )
        message.save()

        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})