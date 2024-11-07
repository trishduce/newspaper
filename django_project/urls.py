# django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("articles/", include("articles.urls")),  # new
    path("", include("pages.urls")),
    path("ratings/", include("star_ratings.urls", namespace="ratings")),
] + debug_toolbar_urls()
