from django.urls import path
from smo.apps import SmoConfig
from smo import views
from django.views.decorators.cache import cache_page

app_name = SmoConfig.name

urlpatterns = [
    path('home/', cache_page(60)(views.HomeView.as_view()), name='home'),
    path('about_us/', cache_page(60)(views.AboutUsView.as_view()), name='about_us'),
    path('services/', cache_page(60)(views.ServicesListView.as_view()), name='services'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
    path('apppointment/', views.ApppointmentCreateView.as_view(), name='apppointment'),
]
