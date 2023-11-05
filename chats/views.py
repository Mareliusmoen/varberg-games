from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Chat, Message

def chats_view(request):
    # Retrieve a list of chat conversations that the logged-in user is a part of
    user = request.user  # Assuming you have user authentication
    chat_conversations = Chat.objects.filter(users=user)

    # You can add more context data if needed
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
    messages = Message.objects.filter(sender=request.user, receiver_id=user_id).order_by('timestamp')

    chat_history = []
    for message in messages:
        chat_history.append({
            'content': message.content,
            'sender_id': message.sender_id,
        })

    return JsonResponse({'messages': chat_history})