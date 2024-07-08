# src/app/restauran/urls.py

# Django dan third parties modules
from django.urls import path

# Locals
from app.restauran import views

# app name
app_name = "restauran"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("menu/", views.menu_view, name="menu"),
    path("reservasi/", views.reservasi_view, name="reservasi"),
]
