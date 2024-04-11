from django.shortcuts import render
from django.views.generic import ListView

from smo.models import Services


def home(request):
    return render(request, 'smo/home.html')


def about_us(request):
    return render(request, 'smo/about-us.html')


class ServicesListView(ListView):
    model = Services


def blog(request):
    return render(request, 'smo/blog.html')


def elements(request):
    return render(request, 'smo/elements.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"{name} {phone} ({email}): {message}")
    return render(request, 'smo/contact.html')
