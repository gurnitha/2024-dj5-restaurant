# src/app/user/urls.py

# Django dan third parties modules
from django.urls import path

# Locals
from app.user import views

# app name
app_name = "user"

urlpatterns = [
    path("register/", views.register_view, name="register"),
]
