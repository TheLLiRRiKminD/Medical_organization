from django.shortcuts import render
from django.views.generic import ListView, View, CreateView
from smo.forms import ApppointmentForm
from smo.models import Services, BlogWriter, Apppointment
from users.models import Doctor
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from config import settings


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


class BlogListView(ListView):
    model = BlogWriter


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


class ApppointmentCreateView(CreateView):
    model = Apppointment
    form_class = ApppointmentForm
    success_url = reverse_lazy('smo:apppointment')

    def form_valid(self, form):
        """ Дружественное письмо на почту пользователя после записи на прием """
        new_apppointment = form.save()
        send_mail(
            subject='Запись на прием к врачу',
            message=f'Вы записались на прием к {new_apppointment.doctors} на {new_apppointment.date}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_apppointment.email],
            fail_silently=False
        )
        return redirect('smo:apppointment')
