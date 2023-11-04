from django.core.management.base import BaseCommand
from django.utils import timezone
from events.models import Event

class Command(BaseCommand):
    help = 'Delete events with a date that has passed'

    def handle(self, *args, **options):
        # register the current time in the now variable
        now = timezone.now()

        # Delete old events with a date that has passed
        deleted_count = Event.objects.filter(date__lt=now).delete()[0]

        self.stdout.write(self.style.SUCCESS(f'Deleted {deleted_count} past events.'))