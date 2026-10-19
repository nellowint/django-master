
from rest_framework import generics

from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer