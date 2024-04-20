from django.contrib import admin

from smo.models import Services, BlogWriter, Apppointment


# Register your models here.

@admin.register(Services)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'icon')


@admin.register(BlogWriter)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')


@admin.register(Apppointment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
