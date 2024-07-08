# src/app/restauran/views.py

# Django dan third parties modules
from django.shortcuts import render

# Create your views here.


def home_view(request):
	return render(request, "restauran/index.html")


def about_view(request):
	return render(request, "restauran/about.html")


def menu_view(request):
	return render(request, "restauran/menu.html")


def reservasi_view(request):
	return render(request, "restauran/reservasi.html")


def kontak_view(request):
	return render(request, "restauran/kontak.html")