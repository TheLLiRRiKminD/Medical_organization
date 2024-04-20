from django.db import models

from users.models import User, Speciality, Doctor

NULLABLE = {'blank': True, 'null': True}


class Services(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, unique=True)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(verbose_name='изображение', upload_to='services/', **NULLABLE)
    icon = models.ImageField(verbose_name='Иконка', upload_to='services/icons/', **NULLABLE)
    doctors = models.ForeignKey(Speciality, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class BlogWriter(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    owner = models.ForeignKey(Doctor, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"


class Apppointment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone_number = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    email = models.EmailField(verbose_name='Почта')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, **NULLABLE, verbose_name='Специализация')
    doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE, **NULLABLE, verbose_name='Доктор')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Записи на прием"