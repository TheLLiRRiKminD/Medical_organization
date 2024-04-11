from django.contrib import admin

from smo.models import Services


# Register your models here.

@admin.register(Services)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image',)