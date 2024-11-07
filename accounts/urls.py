# accounts/urls.py
from django.urls import path
from .views import SignUpView, UserView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("u/", UserView.as_view(), name="u"),
]
