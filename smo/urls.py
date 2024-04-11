from django.urls import path
from smo.apps import SmoConfig
from smo import views

app_name = SmoConfig.name

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('about_us/', views.AboutUsView.as_view(), name='about_us'),
    path('services/', views.ServicesListView.as_view(), name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
]
