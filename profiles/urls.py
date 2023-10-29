from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProfileList.as_view(), name='home'),
]