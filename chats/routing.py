from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'wss/chat/<str:user_id>/', consumers.ChatConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('wss/chat/<str:user_id>/', consumers.ChatConsumer.as_asgi()),
    ])
})