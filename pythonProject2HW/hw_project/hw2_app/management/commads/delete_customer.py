from django.core.management.base import BaseCommand
from hw2_app.models import Customer


class Command(BaseCommand):
    help = "Delete customer by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Customer.objects.filter(pk=pk).first()
        client.delete()
        self.stdout.write(f'{client}')