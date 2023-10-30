from . import views
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('', views.ProfileList.as_view(), name='home'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]