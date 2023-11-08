from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Chat, Message
from django.db.models import Q

def user_search(request):
    search_query = request.GET.get("search_query", "")
    users = User.objects.filter(
        Q(username__icontains=search_query)
        | Q(first_name__icontains=search_query)
        | Q(last_name__icontains=search_query)
    ).values("id", "username", "first_name", "last_name")

    return JsonResponse({"users": list(users)})

def chats_view(request):
    # Retrieve a list of chat conversations that the logged-in user is a part of
    user = request.user
    chat_conversations = Chat.objects.filter(users=user)

    chat_list = []

    for chat in chat_conversations:
        # Get the other user in the chat
        other_user = chat.users.exclude(id=user.id).first()
        chat_list.append({
            'chat': chat,
            'other_user': other_user,
        })

    context = {
        'chat_list': chat_list,
    }

    return render(request, 'chats.html', context)


def fetch_chat_history(request):
    user_id = request.GET.get("user_id")

    # Retrieve the user corresponding to user_id (seller's user ID)
    seller_user = User.objects.get(id=user_id)

    # Check if a chat between the logged-in user and the seller already exists
    existing_chat = Chat.objects.filter(users=request.user).filter(users=seller_user).first()

    if not existing_chat:
        # If a chat doesn't exist, create a new chat and add both users to it
        new_chat = Chat.objects.create(name="Chat Name")
        new_chat.users.add(request.user, seller_user)
    else:
        # If a chat exists, retrieve it
        new_chat = existing_chat

    # Now, fetch and return chat history for the new_chat
    messages = Message.objects.filter(chat=new_chat).order_by('timestamp')

    chat_history = []
    for message in messages:
        chat_history.append({
            'content': message.content,
            'sender': message.sender.username,
        })

    return JsonResponse({'messages': chat_history})


def send_message(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        message_content = request.POST.get("message")

        # Retrieve the user corresponding to user_id
        receiver_user = User.objects.get(id=user_id)

        # Create a Message object and save it to the database, associating it with the chat
        chat, _ = Chat.objects.get_or_create(users=request.user)
        message = Message(
            sender=request.user,
            receiver=receiver_user,
            chat=chat,  # Use the chat field
            content=message_content  # If you want to store the message content
        )
        message.save()

        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})