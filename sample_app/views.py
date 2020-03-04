from django.db.models import F
from django.http import JsonResponse

# Create your views here.
from sample_app.models import NavigationRecord


def last_points(request):
    distinct = NavigationRecord.objects.order_by('vehicle', '-datetime').distinct('vehicle')
    results = NavigationRecord.objects.filter(id__in=distinct).order_by('-datetime').annotate(
        vehicle_plate=F('vehicle__plate')).values('latitude', 'longitude', 'vehicle_plate', 'datetime')
    return JsonResponse(list(results), safe=False)
