from django.urls import path
from smo.apps import SmoConfig
from smo import views

app_name = SmoConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('health/', views.health, name='health'),
    path('medicine/', views.medicine, name='medicine'),
    path('news/', views.news, name='news'),
    path('clients/', views.clients, name='clients'),
    path('contact/', views.contact, name='contact'),
]
