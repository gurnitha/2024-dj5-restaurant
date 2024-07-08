# src/app/blog/views.py

# Django dan third parties modules
from django.shortcuts import render

# Create your views here.


def posts_list_view(request):
	return render(request, "blog/posts-list.html")
