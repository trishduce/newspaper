from django.urls import path
from .views import HomePageView, HomePageView2

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home2/", HomePageView2.as_view(), name="home"),
]
