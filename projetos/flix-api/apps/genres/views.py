
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Genre


@csrf_exempt
def view_genres(request):
    if request.method == 'GET':
        genres = Genre.objects.filter(is_active=True)
        data = [{'id': genre.id, 'name': genre.name} for genre in genres ]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        genre = Genre(name=data['name'])
        genre.save()
        return JsonResponse({'id': genre.id, 'name': genre.name}, status=201)
    else:
        return JsonResponse({'message': 'Erro'}, status=500)


@csrf_exempt
def detail_genres(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'GET':
        return JsonResponse({'id': genre.id, 'name': genre.name})
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse({'id': genre.id, 'name': genre.name})
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message': 'Registro deletado com sucesso'}, status=204)
    else:
        return JsonResponse({'message': 'Erro'}, status=500)