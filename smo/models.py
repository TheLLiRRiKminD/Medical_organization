from django.db import models

from users.models import User, Speciality

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
    slug = models.CharField(max_length=150, verbose_name='Slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"



