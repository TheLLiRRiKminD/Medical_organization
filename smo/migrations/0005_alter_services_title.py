# Generated by Django 5.0.4 on 2024-04-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smo', '0004_services_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
    ]
