from django.core.management.base import BaseCommand, CommandError
from rest_framework_api_key.models import APIKey


class Command(BaseCommand):
    help = "Creates and API key for testing the API"

    def handle(self, *args, **options):
        api_key, key = APIKey.objects.create_key(name="admin-service")

        self.stdout.write(self.style.SUCCESS('API KEY: "%s"' % key))