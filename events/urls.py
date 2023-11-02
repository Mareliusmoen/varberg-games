from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),  # This is for the list of public events
    path('create_event/', views.create_event, name='create_event'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('join_event/<int:event_id>/', views.join_event, name='join_event'),
    path('joined_events/', views.joined_events, name='joined_events'),
    path('events/<int:event_id>/enter_access_code/', views.enter_access_code, name='enter_access_code'),
]