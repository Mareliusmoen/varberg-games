import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user_id = self.scope['url_route']['kwargs']['user_id']
        self.user = self.scope["user"]  # The current user
        self.target_user = User.objects.get(id=user_id)  # The user you are chatting with

        if self.user.is_authenticated and self.user != self.target_user:
            # Check if the current user is authenticated and not chatting with themselves
            self.chat_group_name = f"chat_{self.user.id}_with_{self.target_user.id}"

            await self.channel_layer.group_add(
                self.chat_group_name,
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()
            await self.accept()

        async def disconnect(self, close_code):
            await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope["user"]  # Get the user who sent the message

        # Handle incoming messages
        if user.is_authenticated:
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': user.username,
                }
            )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))