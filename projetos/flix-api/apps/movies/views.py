
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import CustomPermissions
from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions, )
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions, )
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer