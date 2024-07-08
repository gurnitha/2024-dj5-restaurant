# src/config/urls.py

# Django dan third parties modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # admin 
    path("admin/", admin.site.urls),

    # restauran
    path("", include("app.restauran.urls", namespace="restauran")),

    # blog
    path("", include("app.blog.urls", namespace="blog")),
]