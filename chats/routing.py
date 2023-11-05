from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/some_chat/(?P<USER_ID>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
