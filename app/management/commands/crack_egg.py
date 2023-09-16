from django.core.management.base import BaseCommand
from app.models import Egg


class Command(BaseCommand):
    help = 'nothing to see here'

    def handle(self, *args, **kwargs):
        egg = Egg.objects.first()
        egg.health =  0.0
        egg.save()


