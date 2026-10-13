
from django.http import JsonResponse
from .models import Genre

def list_view_genres(request):
    genres = Genre.objects.filter(is_active=True)
    data = [{'id': genre.id, 'name': genre.name} for genre in genres ]
    return JsonResponse(data, safe=False)
