# Generated by Django 5.0.4 on 2024-04-20 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smo', '0007_remove_services_doctor_services_doctors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogwriter',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='blogwriter',
            name='view_count',
        ),
    ]
