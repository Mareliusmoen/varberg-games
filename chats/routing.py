from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('wss/chat/<str:user_id>/', ChatConsumer.as_asgi()),
    ])
})