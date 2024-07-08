# src/app/restauran/urls.py

# Django dan third parties modules
from django.urls import path

# Locals
from app.restauran import views

# app name
app_name = "restauran"

urlpatterns = [
    path("", views.home_view, name="home"),
]
