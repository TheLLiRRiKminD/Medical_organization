from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='e-mail')

    avatar = models.ImageField(upload_to='user/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Speciality(models.Model):
    title = models.CharField(max_length=50, verbose_name='Специализация', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Doctor(models.Model):
    name = models.CharField(max_length=35, verbose_name='Имя')
    photo = models.ImageField(upload_to='user/doctor', verbose_name='фото', **NULLABLE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
