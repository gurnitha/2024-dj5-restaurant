# src/app/blog/urls.py

# Django dan third parties modules
from django.urls import path

# Locals
from app.blog import views

# app name
app_name = "blog"

urlpatterns = [
    path("posts/", views.posts_list_view, name="posts_list"),
]
