from django.urls import path
from . import views

urlpatterns = [
    path("user_search/", views.user_search, name="user_search"),
    path('chats/', views.chats_view, name='chats'),
    path('fetch_chat_history/', views.fetch_chat_history, name='fetch_chat_history'),
    path('send_message/', views.send_message, name='send_message'),
]