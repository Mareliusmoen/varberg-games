from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='events'),
    path('create_event/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
]