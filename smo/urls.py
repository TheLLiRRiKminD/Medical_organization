from django.urls import path

from smo.views import index

urlpatterns = [
    path('', index)
]
