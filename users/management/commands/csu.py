import os

from django.core.management import BaseCommand

from users.models import User
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=f"{os.getenv('EMAIL_ADDRESS')}",
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('SUPASSWORD'))
        user.save()