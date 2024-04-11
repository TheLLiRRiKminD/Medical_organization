from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'smo/home.html')


def health(request):
    return render(request, 'smo/health.html')


def medicine(request):
    return render(request, 'smo/medicine.html')


def news(request):
    return render(request, 'smo/news.html')


def clients(request):
    return render(request, 'smo/client.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"{name} ({email}): {message}")
    return render(request, 'smo/contact.html')
