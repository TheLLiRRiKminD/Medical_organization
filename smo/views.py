from django.shortcuts import render
from django.views.generic import ListView, View
from smo.models import Services
from users.models import User, Doctor


class HomeView(View):

    def get(self, request):
        doctors = Doctor.objects.all()
        services = Services.objects.all()
        return render(request, 'smo/home.html', {'doctors': doctors, 'services': services})


class AboutUsView(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        services = Services.objects.all()
        return render(request, 'smo/about-us.html', {'doctors': doctors, 'services': services})


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
