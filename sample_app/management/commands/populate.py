from datetime import datetime

from django.core.management import BaseCommand

from sample_app.models import Vehicle, NavigationRecord


def populate(vehicle_count, navigation_records_count):
    vehicles = []
    navigation_records = []

    for i in range(vehicle_count):
        vehicles.append(Vehicle(plate=i))
    Vehicle.objects.bulk_create(vehicles)

    for x in range(vehicle_count):
        for y in range(navigation_records_count):
            navigation_records.append(
                NavigationRecord(longitude=1.0, latitude=1.0, vehicle=vehicles[x],
                                 datetime=datetime.now().isoformat() + "Z"))
            # print(x, y)

    NavigationRecord.objects.bulk_create(navigation_records)


class Command(BaseCommand):
    def handle(self, *args, **options):
        populate(options['vehicle_count'], options['navigation_record_count'])

    def add_arguments(self, parser):
        parser.add_argument('vehicle_count', type=int)
        parser.add_argument('navigation_record_count', type=int)
