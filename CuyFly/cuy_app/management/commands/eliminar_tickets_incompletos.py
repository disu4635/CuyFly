from django.core.management.base import BaseCommand
from django.utils import timezone
from cuy_app.models import Ticket

class Command(BaseCommand):
    help = 'Elimina tickets incompletos o expirados.'

    def handle(self, *args, **options):
        tiempo_limite = timezone.now() - timezone.timedelta(minutes=30)

        # Eliminar tickets incompletos o expirados
        Ticket.objects.filter(flight=None, created_at__lt=tiempo_limite).delete()
        Ticket.objects.filter(flight__isnull=False, created_at__lt=tiempo_limite).exclude(
            passengers__isnull=False,
            flight_destination_date__isnull=False,
            flight_arrival_date__isnull=False,
            mobile__isnull=False,
            email__isnull=False,
            seat__isnull=False
        ).delete()

        self.stdout.write(self.style.SUCCESS('Se eliminaron tickets incompletos o expirados.'))
