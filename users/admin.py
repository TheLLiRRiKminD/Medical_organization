from django.contrib import admin
from users.models import User, Speciality, Doctor


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name',)


@admin.register(Speciality)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Doctor)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')