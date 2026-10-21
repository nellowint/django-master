
from rest_framework import generics, permissions

from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer