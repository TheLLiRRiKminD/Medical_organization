from django.db import models

NULLABLE = {'blank': True, 'null': True}


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(verbose_name='изображение', upload_to='news/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(verbose_name='изображение', upload_to='services/', **NULLABLE)
